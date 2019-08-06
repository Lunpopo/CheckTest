# CheckTest

## Description
This script can help you to find out test point you forget in your project.

Supporting python2 temporary.

## Options
```
optional arguments:
  -h, --help            show this help message and exit

get directory module:
  get directory

  -d PATH [PATH ...], --directory PATH [PATH ...]
                        input directory path you want to check

extend module:
  extend command options

  -e REGULAR, --file-extend REGULAR
                        input file extend you wanna check and this option
                        support regular expression, for example -> "*.py" or
                        "*.html"
  -c CHECK-STRING, --check-point CHECK-STRING
                        input the key check point you want to find out and
                        this option support regular expression, for example ->
                        "test|test code|test end"

filter module:
  filter command output module

  -f REGULAR-STRING, --filter REGULAR-STRING
                        filter you do not want to see and this option support
                        regular expression, for example -> "test case | test
                        code"
```

## Simple Example
```
python check_test.py -d test_folder --file-extend '*.py' --check-point 'test|test code|test block|test end' --filter 'test block|test end'
```

## Author
[Lunpopo](https://github.com/Lunpopo/CheckTest)

Its a very light and simple tools for examining the test point you forget in your project.

东西虽小，也有版权，请使用时注明来源，感激不尽！

If you have any question or awesome suggestion please contact me, Thanks a lot! [commit issues](https://github.com/Lunpopo/CheckTest/issues)
