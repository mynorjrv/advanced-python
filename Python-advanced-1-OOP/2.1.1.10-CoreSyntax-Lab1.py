class TimeInterval:
    def __init__(self, hours=0, mins=0, secs=0):
        if not isinstance(hours, int) or hours<0:
            raise TypeError('hours should be int and positive')
        if not isinstance(mins, int) or mins>59 or mins<0:
            raise TypeError('mins should be int between 0 and 59')
        if not isinstance(secs, int) or secs>59 or secs<0:
            raise TypeError('secs should be int between 0 and 59')
        
        self.hours = hours
        self.mins = mins
        self.secs = secs
        
    def __str__(self):
        return f'{self.hours:0>2}:{self.mins:0>2}:{self.secs:0>2}'
        
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError('You can only sum time intervals')
            
        ''' secs = self.secs + other.secs
        
        if secs>60:
            mins = 1
            secs -= 60
        else:
            mins = 0
            
        mins += self.mins + other.mins
        
        if mins>60:
            hours = 1
            mins -= 60
        else:
            hours = 0
            
        hours += self.hours + other.hours
        '''
        secsSelf = self.hours*60*60 + self.mins*60 + self.secs
        secsOther = other.hours*60*60 + other.mins*60 + other.secs
        tsecs = secsSelf + secsOther
        
        hours = tsecs//(60*60)
        mins = (tsecs%(60*60))//60
        secs = (tsecs%(60*60))%60
        
        return TimeInterval(hours, mins, secs)
        
    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError('You can only sum time intervals')
            
        secsSelf = self.hours*60*60 + self.mins*60 + self.secs
        secsOther = other.hours*60*60 + other.mins*60 + other.secs
        tsecs = secsSelf - secsOther
        
        hours = tsecs//(60*60)
        mins = (tsecs%(60*60))//60
        secs = (tsecs%(60*60))%60
        
        return TimeInterval(hours, mins, secs)
        
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('Time intervals can only be multiplied by int')
        
        secsSelf = self.hours*60*60 + self.mins*60 + self.secs
        tsecs = secsSelf*other
        
        hours = tsecs//(60*60)
        mins = (tsecs%(60*60))//60
        secs = (tsecs%(60*60))%60
        
        return TimeInterval(hours, mins, secs)
        
        
a1 = TimeInterval(21, 58, 50)
a2 = TimeInterval(1, 45, 22)

print(a1+a2)
print(a1-a2)
print(a1*2)