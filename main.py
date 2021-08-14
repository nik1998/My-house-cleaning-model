import numpy as np

room_names = ["kitchen", "middle hall", "Dany room", "Nikita room", "Big room", "veranda", "yellow hall"]
room_square = [3.1 * 3.1, 3.1 * 2 + 1.1 * 3.2 + 1.8 * 2 + 0.9 * 1.3, 5.8 * 3.2, 3.1 * 3.1, 5.8 * 3.2, 2.9 * 2.4,
               2.9 * 3.5 + 2.9 * 2]
room_weight = [1.8, 1.6, 1.4, 1.3, 1.6, 1.8, 1.4]
# scale 1 2 3 4 5 = 1,1.2 ... 1.8
#room_weight = [5, 4, 3, 2.5, 4, 5, 3]
k = 2
if __name__ == '__main__':
    print(str(sum(room_square)))
    print(room_names)
    print(room_square)
    n = k ** 6
    ans = np.asarray([1000, 1000, 1000])
    txt = [[[] for i in range(k)]] * 3
    m = 1000
    for i in range(n):
        d = i
        l = [0.0] * k
        r = [[] for i in range(k)]
        for j in range(len(room_names)):
            o = d % k
            d = d // k
            l[o] += room_weight[j] * room_square[j]
            r[o].append(room_names[j])
        z = sorted(l)
        if z[k - 1] - z[0] < np.max(ans):
            ii = np.argmax(ans)
            ans[ii] = z[k - 1] - z[0]
            txt[ii] = r
    d = {}
    for i, n in enumerate(room_names):
        d[n] = room_weight[i] * room_square[i]
    print(str(d) + "\n")
    for i, v in enumerate(ans):
        print(str(v) + " : " + str(txt[i]) + "\n")
