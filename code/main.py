import argparse
import os
from proj1_part1 import filter
from proj1_part2 import hybrid_img_generation

def main():
    """
        To test your program you can run the tests we created– 'filter' and 'hybrid'. To run each test, you must add the corresponding
        flags (outlined below) to specify which test you are running, and the image paths you are running the tests on

        Command line usage: python3 main.py -t | --test <filter or hybrid> -i | --img <image path(s) separated by comma (no spaces)>

        -t | --test - flag - required. specifies which test to run (filter - image filtering or hybrid – hybrid image generation)
        -i | --img - flag - required. specifies which image to filter or images to create a hybrid. If running hybrid should be two image
        paths separated by a comma (no spaces)

        e.g.
        python3 main.py -p filter ../data/dog.bmp
        python3 main.py -p hybrid ../data/cat.bmp,../data/dog.bmp

        """

    # create the command line parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", required=True, help="Either 'filter' to run image filtering or 'hybrid' to run "
                                                            "(hybrid image generation)")
    parser.add_argument("-i", "--img", required=True, help="Paths to image(s). If running hybrid images separate "
                                                           "paths by a comma (no space)")
    args = parser.parse_args()

    # if testing filtering (part 1)
    if args.test == 'filter':
        # if specified path does not exist
        if not os.path.exists(args.img):
            # if used a comma in the file path, user may have
            # tried to run hybrid, remind user they are running filtering
            if (',' in args.img):
                print('You wrote a file path separated by a comma. You only need to specify '
                      'one file path if you are testing filtering.')
            # if no comma used, user input path wrong
            else:
                print('The file path you specified: ' + args.img + ' does not exist. Try running something like: '
                                                                   '\n python3 main.py -p filter -i ../data/dog.bmp')
        # if path does exist, run filter tests
        else:
            print('running filter tests on image ' + args.img)
            filter(args.img)

    # if testing hybrid (part 2)
    elif args.test == 'hybrid':
        img1, img2 = args.img.split(',')
        # check if either of specified image paths don't exist
        if not os.path.exists(img1):
            print('The file path you specified for image 1 does not exist')
        elif not os.path.exists(img2):
            print('The file path you specified for image 2 does not exist')
        # if both paths exist run
        else:
            print('running hybrid image generation tests on images ' + img1 + ' and ' + img2)
            hybrid_img_generation(img1, img2)

    # user didn't specify whether testing filtering or hybrid image generation
    else:
        print("You must specify what you are testing (either 'filter' or 'hybrid')"
              " for e.g. try running: \n python3 main.py -p filter -i ../data/dog.bmp")


if __name__ == '__main__':
    main()
