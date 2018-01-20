# Rough and ugly piece of code for generating rpi_gles2_native.py from gl2.h
# License: Copyleft

import re
import os

def create_gles2():
    with open("/opt/vc/include/GLES2/gl2.h", "rt") as gl_h:
        with open("/home/pi/gles2_native_new.py", "wt") as gl_py:
            for line in gl_h:
                if line.startswith("#define"):
                    m = re.match(r"#define\s+([\w_]+)\s+([a-fA-F\dx]+)", line)
                    if m is None:
                        continue
                    name, value = m.groups()
                    gl_py.write("{} = {}\n".format(name, value))
                elif line.startswith("GL_APICALL"):
                    m = re.match(r"GL_APICALL\s+(?:const\s*)?([\w_\s*]+)\s+GL_APIENTRY\s+([\w_]+)\s*\((.+?)\)\s*;", line)
                    if m is None:
                        continue
                    res, name, params = m.groups()
                    res = res.replace(" ", "")
                    if res == "void":
                        res = "None"
                    argtypes = re.findall(r"(?:const\s*)?([\w_]+\s*\*{1,2}|[\w_]+\s)\s*[\w_]", params)
                    argtypes = [s.replace(" ", "") for s in argtypes]
                    argtypes = [s.replace("*", "_p") for s in argtypes]
                    if len(argtypes) == 1:
                        argtypes = [argtypes[0]+","]
                    res = res.replace("*", "_p")
                    argnames = re.findall(r"[\s*]([\w_]+)\s*,", params + ",")
                    gl_py.write("\"\"\" {line} \"\"\"\n"
                                "gles2.{name}.restype = {res}\n"
                                "gles2.{name}.argtypes = ({argtypes})  # {argnames}\n"
                                "{name} = gles2.{name}\n\n".format(line=line.replace("\n", ""),
                                                                   name=name,
                                                                   res=res,
                                                                   argtypes=", ".join(argtypes),
                                                                   argnames=", ".join(argnames)))

if __name__ == "__main__":
    create_gles2()
    print("Ok!")
