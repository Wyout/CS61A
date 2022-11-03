"""Typing test implementation"""

from curses import flash
from sys import flags
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    new_p = [p for p in paragraphs if select(p)]
    if k >= len(new_p):
        return ''
    return new_p[k]

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select(paragraphy):
        new_paragraphy = split(lower(remove_punctuation(paragraphy)))
        for p in topic:
            if p in new_paragraphy:
                return True
        return False

    return select

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    count = 0
    i = 0
    total = min(len(reference_words), len(typed_words))
    
    if typed_words == []:
        return 0.0
    else:
        while i < total:
            if reference_words[i] == typed_words[i]:
                count += 1
            i += 1
        return count / len(typed_words) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if typed == '':
        return 0.0
    length = len(typed)
    div_five = length / 5
    per_one = elapsed / div_five
    return 60 / per_one
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    # 自己写的感觉没啥问题，基本案例也是对的，但就是过不了
    # if user_word in valid_words:
    #     return user_word
    # else:
    #     min_num = -1
    #     min_dir = -1
    #     for v_word in valid_words:
    #         if min_num == 0:
    #             return valid_words[min_dir]
    #         elif diff_function(user_word, v_word, limit) < min_num or min_num == -1:
    #             min_num = diff_function(user_word, v_word, limit)
    #             min_dir += 1
    #     if min_num > limit:
    #         return user_word
    #     return valid_words[min_dir]

    # 这个是别人的方法，我只借鉴了部分代码和思路（那位作者用了key，燃鹅我看不懂key啥意思，但用while写出来了）
    if user_word in valid_words:
        return user_word
        
    diff_num = [diff_function(user_word, v, limit) for v in valid_words]
    zipped_num_word = list(zip(valid_words, diff_num))
    min_num = min(diff_num)
    i = 0
    length = len(diff_num)

    if min_num > limit:
        return user_word
    while i < length:
        if zipped_num_word[i][1] == min_num:
            return zipped_num_word[i][0]
        i += 1
    
            


    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    # 自己写的，网站上给的例子都可以，但最后还是错了
    # def help(start, goal, limit):
    #     if len(start) == 0 or len(goal) == 0:
    #         return 0 + abs(len(start) - len(goal))
    #     else:
    #         if start[0] != goal[0]:
    #             return 1 + shifty_shifts(start[1:], goal[1:], limit)
    #         else:
    #             return shifty_shifts(start[1:], goal[1:], limit)
    # result = help(start, goal, limit)
    # if result > limit:
    #     return limit + 1
    # return result

    if len(start) == 0:
        return len(goal)
    if len(goal) == 0:
        return len(start)
    if start[0] != goal[0]:
        if limit == 0:
            return 1
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    else:
        return shifty_shifts(start[1:], goal[1:], limit)
        

    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        # 当有一个为0后，剩下的操作只有补或删，故最后是二者相加
        return len(start) + len(goal) 
    elif start[0] == goal[0]:
        # 匹配情况下：二者后进一位，因为没有进行更改操作，所以limit不变
        return pawssible_patches(start[1:], goal[1:], limit)
    else:
        # 不匹配1：因为是添加，所以本来要后进一位的start，因为加了就不需要后进了
        add_diff = pawssible_patches(start, goal[1:], limit-1)
        # 不匹配2：因为是删除，start删除后的字符还要和删除前的goal相比对，故只是start后移
        remove_diff = pawssible_patches(start[1:], goal, limit-1)
        # 不匹配3：因为是替换，替换后都看后一位，故都后移 
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        # 这段我是真的看不懂了
        return 1 + min(min(add_diff, remove_diff), substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # 计算正确率
    # 不知道我写的递归哪错了
    # if typed[0] != prompt[0]:
    #     return 0
    # if len(typed) == 0:
    #     return 0
    # else:
    #     total = 1 + report_progress(typed[1:], prompt[1:], user_id, send)
    # progress = total / len(prompt)

    total = 0
    for t, p in zip(typed, prompt):# 这是一种很厉害的思路啊
        if t == p:
            total += 1
        else:
            break
    progress = total / len(prompt)

    # 使用send
    send({'id': user_id, 'progress': progress})

    # 最后再返回一次progress
    return progress

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    # 计算玩家打字时间
    all = []
    for i in times_per_player:
        part = []
        j = 0
        total = len(i) - 1
        while j < total:
            part += [i[j + 1] - i[j]]
            j += 1
        all += [part]
    return game(words, all)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"

    words = all_words(game) #单词数组
    times = all_times(game) #时间数组
    total_player = len(times) #玩家总数

    # 建立表格表格
    all = [[] for i in range(total_player)]
    
    i = 0
    while i < len(words):
        # 每个单词对应的每个玩家的时间
        word_times = [times[j][i] for j in range(total_player)]
        fastest_t = min(word_times)
        # 找到最快时间对应的下标（玩家）
        k = 0
        while k < total_player:
            if word_times[k] == fastest_t:
                break
            k += 1
        # 把单词放入all中（对应的玩家哪里）
        all[k] += [words[i]]

        i += 1
    return all

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)