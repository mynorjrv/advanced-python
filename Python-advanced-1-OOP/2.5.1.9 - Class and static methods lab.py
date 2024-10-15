import string

class LuxWatch:
    __watches_created = 0
    
    def __init__(self):
        LuxWatch.__watches_created += 1
        self.text = ''
        print('Watch created')
    
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created
        
    @classmethod
    def include_engraving(cls, text):
        LuxWatch.check_engraving(text)
        _watch = LuxWatch()
        _watch.text = text
        print('Watch created with text')
        return _watch
        
    @staticmethod
    def check_engraving(text):
        if len(text)>40:
            raise ValueError('Text should contain at most 40 characters.')
        if not all([i in string.ascii_letters+string.digits for i in text]):
            raise ValueError('Text should be alphanumeric and without blank')
        print('Apropiate text')
    
a = LuxWatch()
b = LuxWatch.include_engraving('Graduacion')

try:
    c = LuxWatch.include_engraving('23#"$#2dsafaf')
except ValueError:
    print('Watch not created')
    
print(LuxWatch.get_number_of_watches_created())