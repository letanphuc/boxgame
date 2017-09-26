import random


class Dice:
    @staticmethod
    def roll(count=2):
        ret = sum([random.randint(1, 6) for _ in range(count)])
        return ret


class Player:
    def __init__(self, choose, name = "PlayerX"):
        self.name = name
        self.start_up_nums = [x for x in range(1, 10)]
        self.is_end = True
        self.choose = choose
        self.current_nums = self.start_up_nums[:]

    def self_play(self, count):
        ret = []
        print 'Player = ', self.name
        for i in range(count):
            self.is_end = False
            self.current_nums = self.start_up_nums[:]
            while not self.is_end:
                s = Dice.roll(1 if self.can_roll_one() else 2)
                avai_chosens = self.get_available_choosens(self.current_nums, s)
                print '  current_nums', self.current_nums, 's = ', s, 'avai_chosens = ', avai_chosens

                if len(avai_chosens) == 0:
                    self.is_end = True
                    print '  Runtime %i, Point = ' %i, self.get_points()
                    print ''
                    ret.append(self.get_points())
                else:
                    chosen = self.choose(avai_chosens)
                    print '  choose: ', chosen
                    self.play(chosen)
        return ret

    def get_points(self):
        tmp = ''.join([str(x) for x in self.current_nums])
        return int(tmp) if len(tmp) > 0 else 0

    def can_roll_one(self):
        return 9 not in self.current_nums and \
               8 not in self.current_nums and \
               7 not in self.current_nums

    def play(self, choose):
        for c in choose:
            self.current_nums.remove(c)


    @staticmethod
    def get_available_choosens(nums, s):
        ret = []
        # 1
        if s in nums:
            ret.append([s])

        # 2
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == s:
                    ret.append([nums[i], nums[j]])

        return ret


def choose_largest_num(avai_chosens):
    tmp = sorted(avai_chosens, key=lambda x: max(x), reverse=True)
    return tmp[0]

def choose_smallest_num(avai_chosens):
    tmp = sorted(avai_chosens, key=lambda x: max(x))
    return tmp[0]

def print_result(result):
    print '  result = ', result
    print '  min =    ', min(result)
    print '  max =    ', max(result)
    print '  avg =    ', sum(result) * 1.0 / len(result)
    print ''

a = Player(choose_largest_num, 'PlayerA')
b = Player(choose_smallest_num, 'PlayerB')
resulta = a.self_play(10000)
resultb = b.self_play(10000)

print 'a play '
print_result(resulta)
print 'b play '
print_result(resultb)