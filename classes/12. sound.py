from wave import open
from struct import Struct
from math import floor
#可以用‘explorer.exe .’ 来打开资源管理器

frame_rate = 11025
#计算音频数据
def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)

#把采样器的输出变为wav文件
def play(sampler, name='song.wav', seconds=2):
    #wave模块的东西，可以在python库查看
    #'wb'指只写模式
    out = open(name, 'wb')
    out.setnchannels(1)#设置声道数
    out.setsampwidth(2)#设置采样字节长度
    out.setframerate(frame_rate)#采样频率

    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        #encode通过采样（sample）计算音频数据，再写入wav文件
        out.writeframes(encode(sample))
        t += 1
    out.close()

#写sampler，这是的采样器是三角波
def tri(frequency, amplitude=0.3):
    #计算周期
    period = frame_rate // frequency
    #真写sampler，这里直接抄我就不管了
    def sampler(t):
        saw_wave  = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

#几个音的频率
c_freq = 261.63
e_freq = 329.63
g_freq = 392.00

#同时放两个音(和弦)
def both(f, g):
    return lambda t: f(t) + g(t)

#让某个音只在一段时间内播放,fade是淡入淡出
def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0 
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

#因为上面的note的第一个参数是函数，所以我们要给tri命名(当然可以直接给)
#后面有函数来写，所以下面给注释掉了
#c, e = tri(c_freq), tri(e_freq)

#开始写谱
#写一个马里奥的评率采样器函数
def mario_at(octave):#octave是八度
    c, e = tri(octave * c_freq), tri(octave * e_freq)
    g, low_g = tri(octave * g_freq), tri(octave * g_freq /2)
    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    z += 1/2
    return song

play(both(mario_at(1), mario_at(1/2)))