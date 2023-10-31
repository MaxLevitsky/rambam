import argparse
import comm_and_s
parser = argparse.ArgumentParser()
parser.add_argument("num",type=int)
parser.add_argument("name",nargs="?")
args=parser.parse_args()
if args.num==1:
    comm_and_s.pythvers()
elif args.num==2:
    comm_and_s.createdir(args.name)
else:
    comm_and_s.listf()
