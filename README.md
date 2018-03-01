# wyplash

This project is a simple test results viewer written in python and Flask.

The main concept of this project a display tool for tests results, without
having to create test cases and test suites prior to running the tests.

Simply reporting a test case result will automatically create the test
if it does not exist, and create its first result.

Some main features are below:
1) REST API for reporting results. Accept single result, or a xUnit style
xml file.
2) Web UI form for manually uploading xUnit-style results file.
3) Viewing test suite or sub-suite easily.


Latest Flask tutorial from Miguel Grinberg:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world