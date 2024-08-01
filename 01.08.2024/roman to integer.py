class Solution:
    def romanToInt(self, u: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        v=0
        w=0
        for i in range(len(u)):
            if i<len(u)-1 and d[u[i]]<d[u[i+1]]:
                v-=d[u[i]]
            else: 
                v+=d[u[i]]
        return v
