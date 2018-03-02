#!/usr/bin/env python

import sys
import os
import datetime
import argparse
import xml.etree.ElementTree as ET

thispath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(thispath)

from app import db
from app.models import Test, TestSuite, TestResult


def process_junit(xml):
    root = ET.fromstring(xml)

    for testcase in root.findall('testcase'):
        file = testcase.attrib['file']
        classname = testcase.attrib['classname']
        line = testcase.attrib['line']
        name = testcase.attrib['name']
        message = ''
        stack = ''
        for f in testcase.findall('./failure'):
            message = f.attrib['message']
            stack = f.text
            print(stack)

        t = Test(name=name, classname=classname, line=line, failure_message=message, stacktrace=stack)
        t.timestamp = datetime.datetime.now()
        t.file = file

        db.session.add(t)
    db.session.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    args = parser.parse_args()

    print('filename = {}'.format(args.filename))

    with open(args.filename) as f:
        txt = f.read()
        process_junit(txt)
