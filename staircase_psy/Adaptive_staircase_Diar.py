#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 15, 2023, at 17:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Adaptive_staircase_Diar'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ActionLab\\Downloads\\staircase_psy\\staircase_psy\\Adaptive_staircase_Diar.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "start_screen" ---
text = visual.TextStim(win=win, name='text',
    text='Instructions/welcome\n\npress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Adap_staircase" ---
trial_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from standard
from syntacts import *
from time import sleep

session = Session()

# Here we create one of the signals 
amp = 1.0
sin = Sine(125) # Standard Frequency of 125Hz
asr = ASR(0.05, 0.5, 0.05) # Attack (A) susain (S) Release (R)
sig2 = sin * asr * amp
response = visual.TextStim(win=win, name='response',
    text="Same or different? \n\nPress 's' for same and 'd' for different",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# --- Initialize components for Routine "thanks" ---
thank = visual.TextStim(win=win, name='thank',
    text='Thank you for participating',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start_screen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
start_screenComponents = [text, key_resp]
for thisComponent in start_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_screen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_screen" ---
for thisComponent in start_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "start_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --------Prepare to start Staircase "stair" --------
# set up handler to look after next chosen value etc
stair = data.StairHandler(startVal=300.0, extraInfo=expInfo,
    stepSizes=[40,40,40,30,30,30,30,20,20,20,20,10,10,10,10,10,10], stepType='lin',
    nReversals=6.0, nTrials=50.0, 
    nUp=1.0, nDown=2.0,
    minVal=90.0, maxVal=400.0,
    originPath=-1, name='stair')
thisExp.addLoop(stair)  # add the loop to the experiment
level = thisStair = 300.0  # initialise some vals

for thisStair in stair:
    currentLoop = stair
    level = thisStair
    
    # --- Prepare to start Routine "Adap_staircase" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    # Run 'Begin Routine' code from standard
    
    # Here we create one of the signals 
    amp = 1.0
    sin = Sine(125) # Standard Frequency of 125Hz
    asr = ASR(0.05, 0.5, 0.05) # Attack (A) susain (S) Release (R)
    sig2 = sin * asr * amp
    
    # Here we create the other signal 
    amp = 1.0
    sin = Sine(level) # Stimulus  
    asr = ASR(0.05, 0.5, 0.05) 
    sig3 = sin * asr * amp
    
    # Here we apply the two signals simultaneously to the audio output channels 
    session.open(6) #
    session.play(0, sig2) # plays sig 1 on channel 0
    session.play(2, sig3) # plays sig 1 on channel 0
    
    sleep(sig2.length)    #plays stimulus for duration of the signal
    # Run 'Begin Routine' code from corr_ans
    if level==125:
        CorrectAns='s'
    else:
        CorrectAns='d'
    # keep track of which components have finished
    Adap_staircaseComponents = [trial_resp, response, ISI]
    for thisComponent in Adap_staircaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Adap_staircase" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and frameN >= 120:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_resp.started')
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['s','d'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(CorrectAns)) or (trial_resp.keys == CorrectAns):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *response* updates
        if response.status == NOT_STARTED and frameN >= 120:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response.started')
            response.setAutoDraw(True)
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ISI.started', t)
            ISI.start(1.0)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 1.0  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Adap_staircaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Adap_staircase" ---
    for thisComponent in Adap_staircaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for stair (StairHandler)
    stair.addResponse(trial_resp.corr, level)
    stair.addOtherData('trial_resp.rt', trial_resp.rt)
    # the Routine "Adap_staircase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# staircase completed


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thank]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank* updates
    if thank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank.frameNStart = frameN  # exact frame index
        thank.tStart = t  # local t and not account for scr refresh
        thank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank.started')
        thank.setAutoDraw(True)
    if thank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            thank.tStop = t  # not accounting for scr refresh
            thank.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thank.stopped')
            thank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
