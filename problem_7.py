class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        str_x = str(x)
        if str_x[0] == '-':
            str_x = str(x)[1:]
            2147483647
            ret = int('-'+str_x[::-1])
            
            if ret < 2147483647 and ret>-2147483647:
                return int('-'+str_x[::-1])
            else:
                return 0
        
        ret =int(str_x[::-1])
        if ret < 2147483647 and ret>-2147483647:
            return int(str_x[::-1])
        else:
            return 0
        