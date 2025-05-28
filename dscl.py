
# MIT License

# Copyright 2024 @asyncze (Michael Sjöberg)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# example usage:
#
# from dscl import dscl
# 
# config = dscl.parse(path_to_config_file)

# example config-file syntax:
#
# [plugins]
# 
# syntax_highlighter      true                  -- enable or disable syntax highlighting plugin
# git_integration         true                  -- enable or disable git integration
# auto_complete           true                  -- enable or disable auto completion
# 
# [themes]
# 
# current_theme           "monokai"             -- set the active theme
# theme_path              "~/.config/themes"    -- path where custom themes are stored
# 
# [logs]
# 
# log_level               "info"                -- set the log level (debug, info, warn, error)
# log_file                "/var/log/editor.log" -- location to store logs

def parse(path) -> dict:
    config = {}
    with open(path, "r") as file:
        content = file.readlines()
        header = None
        config_key = None
        config_value = None

        for line in content:
            if line.strip() == "": continue             # skip empty lines
            if line.strip().startswith("--"): continue  # skip line comment
            
            values = line.split(" ", 1)

            # only headers are length 1
            if len(values) == 1 or (len(values) == 2 and values[1].startswith("--")):
                if values[0].strip().startswith("[") and values[0].strip().endswith("]"):
                    header = values[0].strip().replace("[", "").replace("]", "")
                    config[str(header)] = {}
            
            # all other valid rows are length 2
            elif len(values) == 2:
                config_key = values[0]
                config_value = values[1].strip()
                
                # strip comments
                if "--" in config_value and not config_value.startswith("--"):
                    config_value = config_value.split("--", 1)[0].strip()

                # tuple
                if config_value.startswith("(") and config_value.endswith(")"):
                    config_value = int(config_value)
                    pass

                # strings
                elif config_value.startswith("\"") and config_value.endswith("\""):
                    config_value = config_value.replace("\"", "")
                
                # conditionals
                elif config_value in { "true", "false" }:
                    config_value = True if config_value == "true" else False
                
                # digits
                elif config_value.isdigit():
                    config_value = int(config_value)

                # sanity check
                if config_key != None and config_value != None:
                    config[header][str(config_key)] = config_value

    return config
