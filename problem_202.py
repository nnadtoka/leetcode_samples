class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        s = set()
        d_mult_helper = {}

        # as we will square a lot
        for i in range(10):
            d_mult_helper[str(i)] = i*i

        def get_squared_sum(num):
            l_char = list(str(num))
            l_squared = [d_mult_helper[el] for el in l_char]
            return sum(l_squared)

        res_sum_sq = n
        while res_sum_sq != 1 :
            #print("the iteration value {}".format(res_sum_sq))
            res_sum_sq = get_squared_sum(res_sum_sq)
            #print("sum squared {}".format(res_sum_sq))
            if res_sum_sq in s:
                #print ('set already contains {}'.format(res_sum_sq))
                break
            else:
                s.add(res_sum_sq)
            if res_sum_sq == 1:
                return True
        return False






        
