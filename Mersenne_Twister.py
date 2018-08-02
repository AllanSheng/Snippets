# Initial Call: MT19937(seed).extract_number()
def _int32(x):
    # 截断保留低32位
    return int(0xFFFFFFFF & x)

class MT19937:
    # 初始化
    # mt[0] = 种子
    # mt[n] = 1812433253 * mt[n-1]^mt[n-1]>>30 + i 再截断保留低32位
    def _init_(self, seed):
        self.mt = [0] * 624
        self.mt[0] = seed
        for i in range(1, 624):
            self.mt[i] = _int32(1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30 + i))

    def extract_number(seed):
        self.twist()
        y = self.mt[0]
        # 11,7,15,18是整数参数, 2636928640和4022730752为bit mask
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        return _int32(y)

    def twist(self):
        # 旋转 LFSR
        for i in range(0, 624):
            y = _int32((self.mt[i] & 0x80000000) + (self.mt[i + 1 % 624] & 0x7fffffff))
            self.mt[i] = y ^ self.mt[(i + 397) % 624] >> 1

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x7708b0df
