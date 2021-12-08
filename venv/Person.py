class Person(object):
    def _init_(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


class Talker(Person):
    def _init_(self, name, last_name, age):
        Person._init_(self, name, last_name, age)

    def talk(self, text):
        print(text)


class HappyTalker(Talker):
    def _init_(self, name, last_name, age):
        Talker._init_(self, name, last_name, age)

    def talk(self, text):
        print(text + "!!!")


class SlowTalker(Talker):
    def _init_(self, name, last_name, age):
        Talker._init_(self, name, last_name, age)

    def talk(self, text):
        text = list(text)
        text = " ".join(text)
        print(text)


class StutterTalker(Talker):
    def _init_(self, name, last_name, age):
        Talker._init_(self, name, last_name, age)

    def talk(self, text):
        text = text.split(" ")
        for i in range(len(text)):
            text[i] = text[i][0] * 2 + text[i]
        text = " ".join(text)
        print(text)


def make_them_talk(talker_list, say_what):
    for t in talker_list:
        if t.age > 10:
            print(t.name, end=": ")
            t.talk(say_what)


def main():
    t1 = Talker("regular", "talker", 11)
    t2 = HappyTalker("happy", "talker", 19)
    t3 = SlowTalker("slow", "talker", 15)
    t4 = StutterTalker("stutter", "talker", 16)
    tlist = [t1, t2, t3, t4]
    make_them_talk(tlist, "I love coockies")


if __name__ == '__main__':
    main()
