#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon June 8 2020

@author: ShunIto
"""
import re
import argparse
from PIL import Image, ImageDraw


def main():
    args = get_args()
    with open(args.input, "r") as f:
        lines = f.readlines()

    model = visualise_scenario(lines)
    model.extract()
    model.const()
    model.save_png(args.output)
    model.save_jpg(args.output)
    model.save_eps(args.output)


class visualise_scenario():
    def __init__(self, lines):
        self.lines = lines

    def extract(self):
        pat1 = re.compile(r"([\w\s]*)(?=samples to simulate)")
        pat2 = re.compile(r"([\w\s]*)(?=historical)")
        k = 0
        for l in self.lines:
            k += 1
            if pat1.search(l) != None:
                npop = pat1.search(l).group().strip()
            if pat2.search(l) != None:
                eve = pat2.search(l).group().strip()
                break

        try:
            npop
        except:
            exit()
            print("The number of population was not defined.")

        try:
            eve
        except:
            exit()
            print("No histrical events were found.")

        scenario = []
        for t in range(k, k + int(eve)):
            scenario.append(self.lines[t].split())

        self.npop = int(npop)
        self.eve = int(eve)
        self.scenario = scenario

    def const(self):
        def draw_unit(class_, w1, w2, h1, size=True):
            class_.rectangle((w*w1-2, im.height-h-2, w*w1+2, im.height-h*h1+2), fill=(0, 0, 0), outline=(0, 0, 0))
            if size == True:
                class_.rectangle((w * w1 - 2, im.height - h * h1 - 2, w * w2 + 2, im.height - h * h1 + 2),
                                 fill=(0, 0, 0), outline=(0, 0, 0))
            else:
                class_.rectangle((w*w2-2, im.height-h*h1-2, w*w1+2, im.height-h*h1+2), fill=(0, 0, 0), outline=(0, 0, 0))
            return (class_)
        im = Image.new("RGB", (512, 512), (255, 255, 255))
        h = round(im.height / (self.eve + 3))
        w = round(im.width / (self.npop + 3))
        draw = ImageDraw.Draw(im)
        k = 2
        for s in self.scenario:
            if int(s[1]) < int(s[2]): draw = draw_unit(draw, int(s[1])+1, int(s[2])+1, k)
            else: draw = draw_unit(draw, int(s[1])+1, int(s[2])+1, k, size=False)
            draw.line((w*(self.npop+1)-5, im.height-h*k+2, w*(self.npop+1)+5, im.height-h*k+2), fill=(0,0,0), width=2)
            draw.text((w*(self.npop+1)+7, im.height-h*k+2), "t"+str(k-1), fill=(0,0,0))
            k += 1
        draw.rectangle((w*(int(s[2])+1)-2, im.height-h-2, w*(int(s[2])+1)+2, im.height-h*k+2),
                       fill=(0, 0, 0), outline=(0, 0, 0))
        draw.line((w*(self.npop+1), im.height-h, w*(self.npop+1),
                   im.height-h*(self.eve+2)), fill=(0, 0, 0), width=2)
        draw.polygon([(w*(self.npop+1),im.height-h*(self.eve+2)-4),
                     (w*(self.npop+1)-5,im.height-h*(self.eve+2)+4),
                     (w*(self.npop+1)+5,im.height-h*(self.eve+2)+4)], fill=(0, 0, 0), outline=(0, 0, 0))
        draw.line((w*(self.npop+1)-5, im.height-h, w*(self.npop+1)+5, im.height-h), fill=(0, 0, 0), width=2)
        draw.text((w*(self.npop+1)+7, im.height-h), "0", fill=(0, 0, 0))
        self.im = im

    def show(self):
        self.im.show()

    def save_png(self, output):
        self.im.save(output + ".png")

    def save_jpg(self, output, quality=95):
        self.quality=quality
        self.im.save(output + ".jpg", quality=self.quality)

    def save_eps(self, output):
        self.im.save(output + ".eps")


def get_args():
    parser = argparse.ArgumentParser(
        prog="ABC_par_visualise.py",
        description="Plot ABC phylogeny from par formatted file",
        add_help=True
    )
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    return(args)




if __name__ == '__main__':
    main()
