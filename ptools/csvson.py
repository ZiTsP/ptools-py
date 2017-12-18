'''
Created on Dec 15, 2017

@author: zitsp
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
        'from_csv',
        help='select .csv files',
        nargs = '+',
        type=str)
parser.add_argument(
        '-a', '--add',
        help='to export as additional (default : overriding)',
        action="store_true")
parser.add_argument(
        '-d', '--debug',
        help='Enable debug print()',
        action="store_true")
parser.add_argument(
        '-s', '--separator',
        help='separator of csv (default : ","(single comma))',
        default=',',
        type=str)
parser.add_argument(
        '--header',
        help='if there is no header(column) in input csv (default : read header as columns)',
        action='store_false')
parser.add_argument(
        '--column',
        help='if do not use column (default : use columns if not enable --header option)',
        action='store_false')

_EXT_CSV = '.csv'
_EXT_JSON = '.json'

from putils.pio import ConvExport

if __name__ == '__main__':
    args = parser.parse_args()
    for ff in args.from_csv:
        if ff.endswith(_EXT_CSV):
            ConvExport.csv2json(ff, None, args.separator, args.header, args.column, args.add)
        elif ff.endswith(_EXT_JSON):
            ConvExport.json2csv(ff, None, args.separator, args.add)
        else:
            continue
