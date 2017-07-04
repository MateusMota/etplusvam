#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on maio 03, 2017, at 17:50
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'visual_attention'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\LAPS03\\Documents\\Mateus\\PIBIC\\Toyama\\visual_attention.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1600, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instrucoes"
instrucoesClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Bem vindo ao experimento \n   de Aten\xe7\xe3o Visual\n\nInstru\xe7\xf5es:\n\n1- Ser\xe3o mostradas a seguir algumas imagens.\n2- A primeira fase ser\xe1 de aquecimento, logo\nap\xf3s ser\xe1 aplicado o experimento.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "contagem"
contagemClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Fase de Aquecimento em: 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Fase de Aquecimento em: 2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Fase de Aquecimento em: 1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "mostra_imagens_aquecimento"
mostra_imagens_aquecimentoClock = core.Clock()
image_aquecimento = visual.ImageStim(
    win=win, name='image_aquecimento',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[768, 512],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imagegray = visual.ImageStim(
    win=win, name='imagegray',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "preparacao"
preparacaoClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text=u'a fase de calibrac\xe3o iniciar\xe1 em : 3',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
text3 = visual.TextStim(win=win, name='text3',
    text=u'a fase de calibrac\xe3o iniciar\xe1 em : 2',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text4 = visual.TextStim(win=win, name='text4',
    text=u'a fase de calibrac\xe3o iniciar\xe1 em : 1',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "calibracao"
calibracaoClock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1600, 900),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "preparacao1"
preparacao1Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=u'o experimento iniciar\xe1 em : 3',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text=u'o experimento iniciar\xe1 em : 2',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text=u'o experimento iniciar\xe1 em : 1',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "mostra_imagens"
mostra_imagensClock = core.Clock()
image_1 = visual.ImageStim(
    win=win, name='image_1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=(768, 512),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_gray = visual.ImageStim(
    win=win, name='image_gray',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fim"
fimClock = core.Clock()
text_FIM = visual.TextStim(win=win, name='text_FIM',
    text=u'Obrigado pela participa\xe7\xe3o!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instrucoes"-------
t = 0
instrucoesClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instrucoesComponents = [text, key_resp_2]
for thisComponent in instrucoesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instrucoes"-------
while continueRoutine:
    # get current time
    t = instrucoesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrucoesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucoes"-------
for thisComponent in instrucoesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instrucoes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "contagem"-------
t = 0
contagemClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
contagemComponents = [text_2, text_3, text_4]
for thisComponent in contagemComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "contagem"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = contagemClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # *text_3* updates
    if t >= 1.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # *text_4* updates
    if t >= 2.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    frameRemains = 2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_4.status == STARTED and t >= frameRemains:
        text_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in contagemComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "contagem"-------
for thisComponent in contagemComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loop_0 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\experiment_conditions.xlsx'),
    seed=None, name='loop_0')
thisExp.addLoop(loop_0)  # add the loop to the experiment
thisLoop_0 = loop_0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_0.rgb)
if thisLoop_0 != None:
    for paramName in thisLoop_0.keys():
        exec(paramName + '= thisLoop_0.' + paramName)

for thisLoop_0 in loop_0:
    currentLoop = loop_0
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_0.rgb)
    if thisLoop_0 != None:
        for paramName in thisLoop_0.keys():
            exec(paramName + '= thisLoop_0.' + paramName)
    
    # ------Prepare to start Routine "mostra_imagens_aquecimento"-------
    t = 0
    mostra_imagens_aquecimentoClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    image_aquecimento.setImage(IMAGENS)
    # keep track of which components have finished
    mostra_imagens_aquecimentoComponents = [image_aquecimento, imagegray]
    for thisComponent in mostra_imagens_aquecimentoComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "mostra_imagens_aquecimento"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mostra_imagens_aquecimentoClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_aquecimento* updates
        if t >= 0.0 and image_aquecimento.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_aquecimento.tStart = t
            image_aquecimento.frameNStart = frameN  # exact frame index
            image_aquecimento.setAutoDraw(True)
        frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_aquecimento.status == STARTED and t >= frameRemains:
            image_aquecimento.setAutoDraw(False)
        
        # *imagegray* updates
        if t >= 5.0 and imagegray.status == NOT_STARTED:
            # keep track of start time/frame for later
            imagegray.tStart = t
            imagegray.frameNStart = frameN  # exact frame index
            imagegray.setAutoDraw(True)
        frameRemains = 5.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if imagegray.status == STARTED and t >= frameRemains:
            imagegray.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mostra_imagens_aquecimentoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mostra_imagens_aquecimento"-------
    for thisComponent in mostra_imagens_aquecimentoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_0'


# ------Prepare to start Routine "preparacao"-------
t = 0
preparacaoClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
preparacaoComponents = [text1, text3, text4]
for thisComponent in preparacaoComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "preparacao"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = preparacaoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text1* updates
    if t >= 0.0 and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1.status == STARTED and t >= frameRemains:
        text1.setAutoDraw(False)
    
    # *text3* updates
    if t >= 1.0 and text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3.tStart = t
        text3.frameNStart = frameN  # exact frame index
        text3.setAutoDraw(True)
    frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3.status == STARTED and t >= frameRemains:
        text3.setAutoDraw(False)
    
    # *text4* updates
    if t >= 2.0 and text4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text4.tStart = t
        text4.frameNStart = frameN  # exact frame index
        text4.setAutoDraw(True)
    frameRemains = 2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text4.status == STARTED and t >= frameRemains:
        text4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preparacaoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preparacao"-------
for thisComponent in preparacaoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\calibracao\\experiment_conditions.xlsx'),
    seed=None, name='loop')
thisExp.addLoop(loop)  # add the loop to the experiment
thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop.keys():
        exec(paramName + '= thisLoop.' + paramName)

for thisLoop in loop:
    currentLoop = loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop.keys():
            exec(paramName + '= thisLoop.' + paramName)
    
    # ------Prepare to start Routine "calibracao"-------
    t = 0
    calibracaoClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    image_2.setImage(IMAGENS)
    # keep track of which components have finished
    calibracaoComponents = [image_2]
    for thisComponent in calibracaoComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "calibracao"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = calibracaoClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calibracaoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "calibracao"-------
    for thisComponent in calibracaoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop'


# ------Prepare to start Routine "preparacao1"-------
t = 0
preparacao1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
preparacao1Components = [text_5, text_6, text_7]
for thisComponent in preparacao1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "preparacao1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = preparacao1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 1.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # *text_7* updates
    if t >= 2.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    frameRemains = 2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_7.status == STARTED and t >= frameRemains:
        text_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preparacao1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preparacao1"-------
for thisComponent in preparacao1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
loop_1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('matheus_conditions.xlsx'),
    seed=None, name='loop_1')
thisExp.addLoop(loop_1)  # add the loop to the experiment
thisLoop_1 = loop_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
if thisLoop_1 != None:
    for paramName in thisLoop_1.keys():
        exec(paramName + '= thisLoop_1.' + paramName)

for thisLoop_1 in loop_1:
    currentLoop = loop_1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
    if thisLoop_1 != None:
        for paramName in thisLoop_1.keys():
            exec(paramName + '= thisLoop_1.' + paramName)
    
    # ------Prepare to start Routine "mostra_imagens"-------
    t = 0
    mostra_imagensClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    image_1.setImage(IMAGENS)
    # keep track of which components have finished
    mostra_imagensComponents = [image_1, image_gray]
    for thisComponent in mostra_imagensComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "mostra_imagens"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mostra_imagensClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_1* updates
        if t >= 0.0 and image_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_1.tStart = t
            image_1.frameNStart = frameN  # exact frame index
            image_1.setAutoDraw(True)
        frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_1.status == STARTED and t >= frameRemains:
            image_1.setAutoDraw(False)
        
        # *image_gray* updates
        if t >= 5.0 and image_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_gray.tStart = t
            image_gray.frameNStart = frameN  # exact frame index
            image_gray.setAutoDraw(True)
        frameRemains = 5.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_gray.status == STARTED and t >= frameRemains:
            image_gray.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mostra_imagensComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mostra_imagens"-------
    for thisComponent in mostra_imagensComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_1'


# ------Prepare to start Routine "fim"-------
t = 0
fimClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
fimComponents = [text_FIM]
for thisComponent in fimComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fim"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fimClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_FIM* updates
    if t >= 0.0 and text_FIM.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_FIM.tStart = t
        text_FIM.frameNStart = frameN  # exact frame index
        text_FIM.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_FIM.status == STARTED and t >= frameRemains:
        text_FIM.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fimComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fim"-------
for thisComponent in fimComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
