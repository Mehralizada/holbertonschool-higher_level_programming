#!/usr/bin/python3.8
import importlib.util
import sys

def main():
    module_name = "hidden_4"
    file_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()
