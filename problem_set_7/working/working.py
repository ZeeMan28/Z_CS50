import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    #regex = r'(?P<t1>[0-9:]*).*?to (?P<t2>[0-9:]*)'
    regex = r'(?P<t1>[0-9:]*).*?(?P<AMPM1>[AMP]*) to (?P<t2>[0-9:]*) (?P<AMPM2>[AMP]*)'
    
    match_list = [match.groupdict() for match in re.finditer(regex, s,  re.DOTALL)]
    
    '''
    {'first_time': '9:00', 'second_time': '5:00'}
    '''
    if len(match_list) > 0:
        t1 = match_list[0]['t1']
        ampm1 = match_list[0]['AMPM1']
        t2 = match_list[0]['t2']
        ampm2 = match_list[0]['AMPM2']
        
        if t1.find(':') == -1:
            t1 += ':00'
        if t2.find(':') == -1:
            t2 += ':00'

        (h,m) = [int(s) for s in t1.split(':')]
        
        if h < 0 or h > 12:
            raise ValueError("bad input")
        if m < 0 or m > 59:
            raise ValueError("bad input")
            
        if ampm1 == 'PM' and h < 12:
            h += 12
        if ampm1 == 'AM' and h == 12:
            h = 0
            
        t1_new = f"{h:02}:{m:02}"
            
        (h,m) = [int(s) for s in t2.split(':')]
        
        if h < 0 or h > 12:
            raise ValueError("bad input")
        if m < 0 or m > 59:
            raise ValueError("bad input")
            
        if ampm2 == 'PM' and h < 12:
            h += 12
        if ampm2 == 'AM' and h == 12:
            h = 0
            
        t2_new = f"{h:02}:{m:02}"
        
        return f"{t1_new} to {t2_new}"

    else:
        raise ValueError("bad input")


if __name__ == "__main__":
    main()