import time

def calc(a, b, c, d, e, f, g):
    return((100 * a) + (50 * b) + (20 * c) + (10 * d) + (5 * e) + (2 * f) + g)

start = time.clock()

count = 1

a_max = 2
b_max = 4
c_max = 10
d_max = 20
e_max = 40
f_max = 100
g_max = 200

a = 0

while(a <= a_max):
    b = 0
    
    while(b <= b_max):
        c = 0
        
        while(c <= c_max):
            d = 0
            
            while(d <= d_max):
                e = 0
                
                while(e <= e_max):
                    f = 0
                    
                    while(f <= f_max):
                        g = 0
                        
                        while(g <= g_max):
                            value = calc(a, b, c, d, e, f, g)
                            if(value == 200):
                                count = count + 1
                                break
                            elif(value < 200):
                                g = g + 1
                            else:
                                break
                        ##f_loop
                        f = f + 1
                    #e_loop
                    e = e + 1
                #d_loop
                d = d + 1
            #c_loop
            c = c + 1
        #b_loop
        b = b + 1
    #a_loop
    a = a + 1

    
print(count)


end = time.clock()
print end - start
