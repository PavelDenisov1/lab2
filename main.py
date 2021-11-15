import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input', default='input.txt')
parser.add_argument('output', default='output.txt')
namespace = parser.parse_args()
inputPath = namespace.input
outputPath = namespace.output
print(inputPath)
print(outputPath)
