
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

            if len(values) == 1:
                header = values[0].strip().replace("[", "").replace("]", "")
                config[str(header)] = {}
            else:
                config_key = values[0]
                config_value = values[1].strip().replace("\"", "")

                if "--" in config_value and not config_value.startswith("--"): config_value = config_value.split("--", 1)[0].strip()

                if config_value == "true": config_value = True
                elif config_value == "false": config_value = False
                elif config_value.isdigit(): config_value = int(config_value)

                if config_key != None and config_value != None: config[header][str(config_key)] = config_value

    return config
