import os
from time import sleep
from subprocess import call, Popen
import webbrowser
import platform
import documentation_manager
import automacdoc

if __name__ == "__main__":
    source_path = r"/home/xanghi/Desktop/github-repos/stibium/example"
    output_path = r"/home/xanghi/Desktop/github-repos/output"

    documentation_manager.DocumentationManager(source_path, output_path, platform.system())
    # automacdoc.write_doc(source_path, output_path)

    sleep(1)

    os.chdir(output_path)

    call(["mkdocs", "build", "--clean"])
    Popen(["mkdocs", "serve"])

    sleep(2)

    webbrowser.open("http://127.0.0.1:8000/")
