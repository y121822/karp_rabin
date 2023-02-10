import sys
import random


class RabinKarp:
    def __init__(self, tmpl, txt):
        self.tmpl, self.txt = tmpl, txt
        self.tmpl_l, self.txt_l = len(self.tmpl), len(self.txt)
        if self.tmpl_l and self.txt_l >= self.tmpl_l:
            self.p = self.tmpl_l * 10**6
            self.x, self.pox = random.randint(1, self.p-1), 1
            self.tmpl_h = self.txt_h = 0
            self.init_hash()
            self.process()

    def init_hash(self):
        for i in range(self.tmpl_l):
            if i:
                self.pox = pow(self.x, i, self.p)
            self.tmpl_h += (ord(self.tmpl[self.tmpl_l-1-i]) * self.pox) % self.p
            self.txt_h += (ord(self.txt[self.tmpl_l-1-i]) * self.pox) % self.p

        self.tmpl_h = self.tmpl_h % self.p
        self.txt_h = self.txt_h % self.p

    def crawl_hash(self, i):
        return ((self.txt_h - ord(self.txt[i]) * self.pox) * self.x +
                ord(self.txt[i+self.tmpl_l])) % self.p

    def process(self):
        for i in range((self.txt_l-self.tmpl_l) + 1):
            if i:
                self.txt_h = self.crawl_hash(i-1)
            if self.tmpl_h == self.txt_h and self.txt[i: i + self.tmpl_l] == self.tmpl:
                print(i, end=' ')


if __name__ == "__main__":
    reader = sys.stdin
    RabinKarp(next(reader).strip(), next(reader).strip())