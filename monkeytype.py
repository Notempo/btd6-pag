import sys
import random
import pygame
from pygame.locals import *
pygame.init()

list = ["the","be","of","and","a","to","in","he","have","it","that","for","they","I","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can","more","if","no","man","out","other","so","what","time","up","go","about","than","into","could","state","only","new","year","some","take","come","these","know","see","use","get","like","then","first","any","work","now","may","such","give","over","think","most","even","find","day","also","after","way","many","must","look","before","great","back","through","long","where","much","should","well","people","down","own","just","because","good","each","those","feel","seem","how","high","too","place","little","world","very","still","nation","hand","old","life","tell","write","become","here","show","house","both","between","need","mean","call","develop","under","last","right","move","thing","general","school","never","same","another","begin","while","number","part","turn","real","leave","might","want","point","form","off","child","few","small","since","against","ask","late","home","interest","large","person","end","open","public","follow","during","present","without","again","hold","govern","around","possible","head","consider","word","program","problem","however","lead","system","set","order","eye","plan","run","keep","face","fact","group","play","stand","increase","early","course","change","help","line"]
dict = {"the": "-T", "be": "-B", "of": "-F", "and": "SKP", "a": "AEU", "to": "TO", "in": "TPH", "he": "E", "have": "SR", "it": "T", "that": "THA", "for": "TP-R", "they": "THE", "I": "EU", "with": "W", "as": "AS", "not": "TPHOT", "on": "OPB", "she": "SHE", "at": "AT", "by": "PWEU", "this": "TH", "we": "WE", "you": "U", "do": "TKO", "but": "PWUT", "from": "TPR", "or": "OR", "which": "WEU", "one": "WUPB", "would": "WO", "all": "AUL", "will": "HR", "there": "THR", "say": "SAEU", "who": "WHO", "make": "PHAEUBG", "when": "WH", "can": "K", "more": "PHOR", "if": "TP", "no": "TPHO", "man": "PHAPB", "out": "OUT", "other": "OER", "so": "SO", "what": "WHA", "time": "TAOEUPL", "up": "UP", "go": "TKPW", "about": "PW", "than": "THAPB", "into": "TPHAO", "could": "KO", "state": "STAEUT", "only": "OEPBL", "new": "TPHU", "year": "KWRAO*EU", "some": "SOPL", "take": "TAEUBG", "come": "KOPL", "these": "THAOES", "know": "TPHOE", "see": "SAOE", "use": "AOUS", "get": "TKPWET", "like": "HRAOEUBG", "then": "THEPB", "first": "TPEURS", "any": "TPHEU", "work": "WORBG", "now": "TPHOU", "may": "PHAEU", "such": "SUFP", "give": "TKPWEUF", "over": "OEFR", "think": "THEU", "most": "PHOFT", "even": "AOEFPB", "find": "TPAOEUPBD", "day": "TKAEU", "also": "HR-S", "after": "AF", "way": "WAEU", "many": "PHA*EPB", "must": "PHUFT", "look": "HRAOBG", "before": "PW-F", "great": "TKPWRAET", "back": "PWABG", "through": "THRU", "long": "HROPBG", "where": "W-R", "much": "PHUFP", "should": "SHO", "well": "WEL", "people": "P", "down": "TKOUPB", "own": "OEPB", "just": "SKWRUFT", "because": "PWAUS", "good": "TKPWAOD", "each": "AOEFP", "those": "THOES", "feel": "TPAOEL", "seem": "SAOEPL", "how": "HOU", "high": "HAOEU", "too": "TAO", "place": "PHRAEUS", "little": "HREUL", "world": "WORL", "very": "SRE", "still": "STEUL", "nation": "TPHAGS", "hand": "HAPBD", "old": "OLD", "life": "HRAOEUF", "tell": "TEL", "write": "WRAOEUT", "become": "PW-BG", "here": "HAOER", "show": "SHOE", "house": "HOUS", "both": "PWO*T", "between": "TWAOEPB", "need": "TPHAOED", "mean": "PHAOEPB", "call": "KAUL", "develop": "SREL", "under": "TPH-PB", "last": "HRAFT", "right": "RAOEUT", "move": "PHAOUF", "thing": "THEUPBG", "general": "SKWREPBL", "school": "SKAOL", "never": "TPHEFR", "same": "SAEUPL", "another": "TPHOER", "begin": "TKPWEUPB", "while": "WHAOEUL", "number": "TPHURPL", "part": "PART", "turn": "TURPB", "real": "RAEL", "leave": "HRAO*EF", "might": "PHAOEUT", "want": "WAPBT", "point": "POEUPBT", "form": "TPORPL", "off": "OF", "child": "KWAOEULD", "few": "TPAOU", "small": "SPHAUL", "since": "SEUPBS", "against": "TKPWEPBS", "ask": "AFBG", "late": "HRAEUT", "home": "HOEPL", "interest": "TR", "large": "HRARPBLG", "person": "PERPB", "end": "EPBD", "open": "OEP", "public": "PHREUBG", "follow": "TPOL", "during": "TKURG", "present": "PREPBT", "without": "WOUT", "again": "TKPWEPB", "hold": "HOLD", "govern": "TKPWOFRPB", "around": "ARPBD", "possible": "POB", "head": "HED", "consider": "KR", "word": "WORD", "program": "PRAPL", "problem": "PRO*B", "however": "HOUFR", "lead": "HRAOED", "system": "S-PL", "set": "SET", "order": "ORD", "eye": "AOEU", "plan": "PHRAPB", "run": "RUPB", "keep": "KAOEP", "face": "TPAEUS", "fact": "TPABGT", "group": "TKPWRAOUP", "play": "PHRAEU", "stand": "STAPBD", "increase": "KRAO*ES", "early": "ERL", "course": "KORS", "change": "KHAEUPBG", "help": "HEP", "line": "HRAOEUPB"}
fps = 1000
fpsClock = pygame.time.Clock()
width, height = 400,300
screen = pygame.display.set_mode((width, height))
text = " "
prompt = list[random.randint(0,199)]
guide = dict.get(prompt)

while True:
  screen.fill("#000000")
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == pygame.K_BACKSPACE:
        text = ""
      else:
        text += event.unicode
  if prompt in text:
    prompt = list[random.randint(0,199)]
    guide = dict.get(prompt)
    text = ""
  font = pygame.font.Font(None, 32)
  color = "#FFFFFF"
  surface1 = font.render(prompt, True, color)
  surface2 = font.render(guide, True, color)
  screen.blit(surface1,(50,50))
  screen.blit(surface2,(50,100))
  pygame.display.flip()
  fpsClock.tick(fps)