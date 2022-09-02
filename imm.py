import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', help="Route")
parser.add_argument("--m", '--model', help="Model yaratish uchun")
parser.add_argument("--r", '--route', help="Route yaratish uchun")
parser.add_argument("--s", '--schema', help="Chema yaratish uchun")
args = parser.parse_args()

# route yaratish
if args.name and args.route:
    print('ergw')

# model yaratish

# schema yaratish