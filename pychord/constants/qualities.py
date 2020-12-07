# -*- coding, utf-8 -*-

from collections import OrderedDict

QUALITY_DICT = OrderedDict((
    # chords consist of 2 notes
    ('5', (0, 7)),
    # 3 notes
    ('sus4', (0, 5, 7)),
    ('sus', (0, 5, 7)),
    ('7no5', (0, 4, 10)),
    ('aug', (0, 4, 8)),
    ('+', (0, 4, 8)),
    ('+5', (0, 4, 8)),
    ('^#5', (0, 4, 8)),
    ('M', (0, 4, 7)),
    ('^', (0, 4, 7)),
    ('', (0, 4, 7)),
    ('maj', (0, 4, 7)),
    ('Mb5', (0, 4, 6)),
    ('m#5', (0, 3, 8)),
    ('-#5', (0, 3, 8)),
    ('m+', (0, 3, 8)),
    ('m', (0, 3, 7)),
    ('min', (0, 3, 7)),
    ('-', (0, 3, 7)),
    ('dim', (0, 3, 6)),
    ('°', (0, 3, 6)),
    ('o', (0, 3, 6)),
    ('sus2', (0, 2, 7)),
    # 4 notes
    ('2', (0, 4, 7, 14)),
    ('4', (0, 5, 10, 15)),
    ('6', (0, 4, 7, 9)),
    ('7', (0, 4, 7, 10)),
    ('M7#5sus4', (0, 5, 8, 11)),
    ('7#5sus4', (0, 5, 8, 10)),
    ('M7sus4', (0, 5, 7, 11)),
    ('7sus4', (0, 5, 7, 10)),
    ('7sus', (0, 5, 7, 10)),
    ('M7+5', (0, 4, 8, 11)),
    ('M7b6', (0, 4, 8, 11)),
    ('^7b6', (0, 4, 8, 11)),
    ('maj7#5', (0, 4, 8, 11)),
    ('maj7+5', (0, 4, 8, 11)),
    ('+maj7', (0, 4, 8, 11)),
    ('^7#5', (0, 4, 8, 11)),
    ('7+5', (0, 4, 8, 10)),
    ('7#5', (0, 4, 8, 10)),
    ('+7', (0, 4, 8, 10)),
    ('7+', (0, 4, 8, 10)),
    ('7aug', (0, 4, 8, 10)),
    ('aug7', (0, 4, 8, 10)),
    ('7b13', (0, 4, 10, 20)),
    ('7-13', (0, 4, 10, 20)),
    ('maj7', (0, 4, 7, 11)),
    ('Δ', (0, 4, 7, 11)),
    ('ma7', (0, 4, 7, 11)),
    ('M7', (0, 4, 7, 11)),
    ('Maj7', (0, 4, 7, 11)),
    ('^7', (0, 4, 7, 11)),
    ('dom', (0, 4, 7, 10)),
    ('add6', (0, 4, 7, 9)),
    ('add13', (0, 4, 7, 9)),
    ('M6', (0, 4, 7, 9)),
    ('M7b5', (0, 4, 6, 11)),
    ('7b5', (0, 4, 6, 10)),
    ('mb6M7', (0, 3, 8, 11)),
    ('m7#5', (0, 3, 8, 10)),
    ('m/ma7', (0, 3, 7, 11)),
    ('m/maj7', (0, 3, 7, 11)),
    ('mM7', (0, 3, 7, 11)),
    ('mMaj7', (0, 3, 7, 11)),
    ('m/M7', (0, 3, 7, 11)),
    ('-Δ7', (0, 3, 7, 11)),
    ('mΔ', (0, 3, 7, 11)),
    ('-^7', (0, 3, 7, 11)),
    ('m7', (0, 3, 7, 10)),
    ('min7', (0, 3, 7, 10)),
    ('mi7', (0, 3, 7, 10)),
    ('-7', (0, 3, 7, 10)),
    ('m6', (0, 3, 7, 9)),
    ('-6', (0, 3, 7, 9)),
    ('oM7', (0, 3, 6, 11)),
    ('m7-5', (0, 3, 6, 10)),
    ('m7b5', (0, 3, 6, 10)),
    ('ø', (0, 3, 6, 10)),
    ('-7b5', (0, 3, 6, 10)),
    ('h7', (0, 3, 6, 10)),
    ('h', (0, 3, 6, 10)),
    ('dim6', (0, 3, 6, 9)),
    ('dim7', (0, 3, 6, 9)),
    ('°7', (0, 3, 6, 9)),
    ('o7', (0, 3, 6, 9)),
    ('quartal', (0, 5, 10, 15)),
    ('madd4', (0, 3, 5, 7)),
    ('+add#9', (0, 4, 8, 15)),
    ('sus24', (0, 2, 5, 7)),
    ('sus4add9', (0, 2, 5, 7)),
    ('9no5', (0, 4, 10, 14)),
    ('M#5add9', (0, 4, 8, 14)),
    ('+add9', (0, 4, 8, 14)),
    ('Madd9', (0, 4, 7, 14)),
    ('add9', (0, 4, 7, 14)),
    ('add2', (0, 4, 7, 14)),
    ('madd9', (0, 3, 7, 14)),
    ('alt7', (0, 4, 10, 13)),
    ('Maddb9', (0, 4, 7, 13)),
    ('mb6b9', (0, 3, 8, 13)),
    ('add11', (0, 4, 7, 17)),
    # 5 notes
    ('9', (0, 4, 7, 10, 14)),
    ('11', (0, 7, 10, 14, 17)),
    ('67', (0, 4, 7, 10, 21)),
    ('69', (0, 4, 7, 9, 14)),
    ('7add6', (0, 4, 7, 10, 21)),
    ('7add13', (0, 4, 7, 10, 21)),
    ('7b6', (0, 4, 7, 8, 10)),
    ('maj#4', (0, 4, 7, 11, 18)),
    ('Δ#4', (0, 4, 7, 11, 18)),
    ('Δ#11', (0, 4, 7, 11, 18)),
    ('M7#11', (0, 4, 7, 11, 18)),
    ('^7#11', (0, 4, 7, 11, 18)),
    ('maj7#11', (0, 4, 7, 11, 18)),
    ('7+11', (0, 4, 7, 10, 18)),
    ('7#11', (0, 4, 7, 10, 18)),
    ('7#4', (0, 4, 7, 10, 18)),
    ('M6#11', (0, 4, 7, 9, 18)),
    ('M6b5', (0, 4, 7, 9, 18)),
    ('6#11', (0, 4, 7, 9, 18)),
    ('6b5', (0, 4, 7, 9, 18)),
    ('mMaj7b6', (0, 3, 7, 8, 11)),
    ('o7M7', (0, 3, 6, 9, 11)),
    ('m7add11', (0, 3, 7, 10, 17)),
    ('m7add4', (0, 3, 7, 10, 17)),
    ('7#5#9', (0, 4, 8, 10, 15)),
    ('7#9#5', (0, 4, 8, 10, 15)),
    ('7alt', (0, 4, 8, 10, 15)),
    ('7+9', (0, 4, 7, 10, 15)),
    ('7#9', (0, 4, 7, 10, 15)),
    ('M9#5sus4', (0, 5, 8, 11, 14)),
    ('M9sus4', (0, 5, 7, 11, 14)),
    ('9sus4', (0, 5, 7, 10, 14)),
    ('9sus', (0, 5, 7, 10, 14)),
    ('13no5', (0, 4, 10, 14, 21)),
    ('maj9#5', (0, 4, 8, 11, 14)),
    ('Maj9#5', (0, 4, 8, 11, 14)),
    ('9#5', (0, 4, 8, 10, 14)),
    ('9+', (0, 4, 8, 10, 14)),
    ('9+5', (0, 4, 8, 10, 14)),
    ('9b13', (0, 4, 10, 14, 20)),
    ('maj9', (0, 4, 7, 11, 14)),
    ('M9', (0, 4, 7, 11, 14)),
    ('Δ9', (0, 4, 7, 11, 14)),
    ('^9', (0, 4, 7, 11, 14)),
    ('6/9', (0, 4, 7, 9, 14)),
    ('M69', (0, 4, 7, 9, 14)),
    ('M9b5', (0, 4, 6, 11, 14)),
    ('9b5', (0, 4, 6, 10, 14)),
    ('7-5', (0, 4, 6, 10, 14)),
    ('9-5', (0, 4, 6, 10, 14)),
    ('m9#5', (0, 3, 8, 10, 14)),
    ('mM9', (0, 3, 7, 11, 14)),
    ('mMaj9', (0, 3, 7, 11, 14)),
    ('-^9', (0, 3, 7, 11, 14)),
    ('m9', (0, 3, 7, 10, 14)),
    ('-9', (0, 3, 7, 10, 14)),
    ('m69', (0, 3, 7, 9, 14)),
    ('-69', (0, 3, 7, 9, 14)),
    ('m9b5', (0, 2, 3, 6, 10)),
    ('b9sus', (0, 5, 7, 10, 13)),
    ('phryg', (0, 5, 7, 10, 13)),
    ('7b9sus', (0, 5, 7, 10, 13)),
    ('7b9sus4', (0, 5, 7, 10, 13)),
    ('11b9', (0, 7, 10, 13, 17)),
    ('7#5b9', (0, 4, 8, 10, 13)),
    ('7b9#5', (0, 4, 8, 10, 13)),
    ('M7b9', (0, 4, 7, 11, 13)),
    ('7b9', (0, 4, 7, 10, 13)),
    ('7-9', (0, 4, 7, 10, 13)),
    # 6 notes
    ('13', (0, 4, 7, 10, 14, 21)),
    ('7#11b13', (0, 4, 7, 10, 18, 20)),
    ('7b5b13', (0, 4, 7, 10, 18, 20)),
    ('13+11', (0, 4, 7, 10, 18, 21)),
    ('13+9', (0, 4, 7, 10, 15, 21)),
    ('13#9', (0, 4, 7, 10, 15, 21)),
    ('7#9b13', (0, 4, 7, 10, 15, 20)),
    ('maj7#9#11', (0, 4, 7, 11, 15, 18)),
    ('7#9#11', (0, 4, 7, 10, 15, 18)),
    ('7b5#9', (0, 4, 7, 10, 15, 18)),
    ('7#9b5', (0, 4, 7, 10, 15, 18)),
    ('13sus4', (0, 5, 7, 10, 14, 21)),
    ('13sus', (0, 5, 7, 10, 14, 21)),
    ('maj13', (0, 4, 7, 11, 14, 21)),
    ('Maj13', (0, 4, 7, 11, 14, 21)),
    ('^13', (0, 4, 7, 11, 14, 21)),
    ('M7add13', (0, 4, 7, 9, 11, 14)),
    ('13b5', (0, 4, 6, 9, 10, 14)),
    ('9#5#11', (0, 4, 8, 10, 14, 18)),
    ('maj9#11', (0, 4, 7, 11, 14, 18)),
    ('Δ9#11', (0, 4, 7, 11, 14, 18)),
    ('^9#11', (0, 4, 7, 11, 14, 18)),
    ('9+11', (0, 4, 7, 10, 14, 18)),
    ('9#11', (0, 4, 7, 10, 14, 18)),
    ('9+4', (0, 4, 7, 10, 14, 18)),
    ('9#4', (0, 4, 7, 10, 14, 18)),
    ('69#11', (0, 4, 7, 9, 14, 18)),
    ('m13', (0, 3, 7, 10, 14, 21)),
    ('-13', (0, 3, 7, 10, 14, 21)),
    ('mMaj9b6', (0, 3, 7, 8, 11, 14)),
    ('m11A', (0, 3, 8, 10, 14, 17)),
    ('m11', (0, 3, 7, 10, 14, 17)),
    ('-11', (0, 3, 7, 10, 14, 17)),
    ('7sus4b9b13', (0, 5, 7, 10, 13, 20)),
    ('7b9b13sus4', (0, 5, 7, 10, 13, 20)),
    ('13-9', (0, 4, 7, 10, 13, 21)),
    ('13b9', (0, 4, 7, 10, 13, 21)),
    ('7b9b13', (0, 4, 7, 10, 13, 20)),
    ('7#5b9#11', (0, 4, 8, 10, 13, 18)),
    ('7b9#11', (0, 4, 7, 10, 13, 18)),
    ('7b5b9', (0, 4, 7, 10, 13, 18)),
    ('7b9b5', (0, 4, 7, 10, 13, 18)),
    ('7b9#9', (0, 4, 7, 10, 13, 15)),
    # 7 notes
    ('13#9#11', (0, 4, 7, 10, 15, 18, 21)),
    ('7#9#11b13', (0, 4, 7, 10, 15, 18, 20)),
    ('M13#11', (0, 4, 7, 11, 14, 18, 21)),
    ('maj13#11', (0, 4, 7, 11, 14, 18, 21)),
    ('M13+4', (0, 4, 7, 11, 14, 18, 21)),
    ('M13#4', (0, 4, 7, 11, 14, 18, 21)),
    ('13#11', (0, 4, 7, 10, 14, 18, 21)),
    ('13+4', (0, 4, 7, 10, 14, 18, 21)),
    ('13#4', (0, 4, 7, 10, 14, 18, 21)),
    ('9#11b13', (0, 4, 7, 10, 14, 18, 20)),
    ('9b5b13', (0, 4, 7, 10, 14, 18, 20)),
    ('13b9#11', (0, 4, 7, 10, 13, 18, 21)),
    ('7b9b13#11', (0, 4, 7, 10, 13, 18, 20)),
    ('7b9#11b13', (0, 4, 7, 10, 13, 18, 20)),
    ('7b5b9b13', (0, 4, 7, 10, 13, 18, 20)),
))
