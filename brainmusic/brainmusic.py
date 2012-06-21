#!/usr/bin/env python

# Copyright (C) 2001 Maurizio Umberto Puxeddu
from __future__ import generators

from pythonsound.table import SimpleHarmonics
from pythonsound.opcode import AOscil, KLinen
from pythonsound import Scheduler, Event, render

import csv
reader = csv.reader(open('../../PDYN.txt', 'rb'), delimiter='\t', quotechar='"')

for row in reader:
	brain1=', '.join(row[1:-1])

a=eval(brain1)
brain1=list(a)

##table1 = SimpleHarmonics(8192, -12.0)

def Instr1(duration, frequency, amplitude, attack, decay):    
    envelope = KLinen(duration, amplitude, attack, decay)
    signal = AOscil(duration, envelope, frequency, brain1)

    while 1: yield signal.next()

scheduler = Scheduler()
    
for n in range(400): scheduler << Event(2.2 * n, AOscil, 1.3 + 0.02 * n, 9000.0, 620.0, brain1)
for n in range(400): scheduler << Event(1.0 * n + 0.5, AOscil, 1.0, 4000.0, 10.0 * (1 + 0.5 * n), brain1)
scheduler << Event(3.0, Instr1, 3.5, 3000.0, 6000.0, 3.0, 2.5)
    
render('brainmusic.wav', scheduler)

##try clustering data in R first, or sorting by the colnames to get similar regions close to each other
