'''
  From a given list of numbers, only the first and last numbers can be chosen
  at a given point in time. There are two players 'A' & 'B'. They get to pick
  up the numbers in turn. Player 'A' starts first. Pick a winning sequence of
  numbers for 'A' and 'B' so that 'A' wins always, no matter how well 'B' plays.
  Assume that both 'A' and 'B' picks the best numbers possible.
  Note: It can be shown that 'A' will always win.
'''

def win_for_a(numbers, total_a, total_b, seq_a, seq_b):
    '''
       Finds a winning strategy for 'A' assuming 'B' picks the best
       numbers.
    '''
    seq_a_copy0 = seq_a[:]
    seq_a_copy1 = seq_a[:]
    seq_b_copy0 = seq_b[:]
    seq_b_copy1 = seq_b[:]
    seq_a_copy0.append(numbers[0])
    result1 = win_for_b(numbers[1:], total_a + numbers[0], total_b,\
                        seq_a_copy0, seq_b_copy0)
    seq_a_copy1.append(numbers[-1])
    result2 = win_for_b(numbers[:-1], total_a + numbers[-1], total_b,\
                        seq_a_copy1, seq_b_copy1)
    if result1[0] > result2[0]:
        return (result1[0], result1[1], result1[2], result1[3])
    else:
        return (result2[0], result2[1], result2[2], result2[3])

def win_for_b(numbers, total_a, total_b, seq_a, seq_b):
    '''
       Finds a winning strategy for 'B' assuming 'A' picks the best
       numbers.
    '''
    seq_a_copy0 = seq_a[:]
    seq_a_copy1 = seq_a[:]
    seq_b_copy0 = seq_b[:]
    seq_b_copy1 = seq_b[:]
    if len(numbers) == 1:
        seq_b_copy0.append(numbers[0])
        return (total_a, total_b + numbers[0], seq_a_copy0, seq_b_copy0)
    else:
        seq_b_copy0.append(numbers[0])
        result1 = win_for_a(numbers[1:], total_a, total_b + numbers[0],\
                            seq_a_copy0, seq_b_copy0)
        seq_b_copy1.append(numbers[-1])
        result2 = win_for_a(numbers[:-1], total_a, total_b + numbers[-1],\
                            seq_a_copy1, seq_b_copy1)
        if result1[1] > result2[1]:
            return (result1[0], result1[1], result1[2], result1[3])
        else:
            return (result2[0], result2[1], result2[2], result2[3])


NUMS = range(1, 11)
print NUMS
SOLUTION = win_for_a(NUMS, 0, 0, [], [])
print 'A\'s sum: %d '  % (SOLUTION[0])
print 'A\'s picks: '
print SOLUTION[2]
print ''
print 'B\'s sum: %d '  % (SOLUTION[1])
print 'B\'s picks: '
print SOLUTION[3]

