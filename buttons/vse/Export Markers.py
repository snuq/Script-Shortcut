import bpy
import math


def get_fps(scene=None):
    if scene is None:
        scene = bpy.context.scene
    return scene.render.fps / scene.render.fps_base


def timecode_from_frames(frame, fps, levels=0, subsecond_type='miliseconds', mode='string'):
    """Converts a frame number to a standard timecode in the format: HH:MM:SS:FF
    Arguments:
        frame: Integer, frame number to convert to a timecode
        fps: Integer, number of frames per second if using 'frames' subsecond type
        levels: Integer, limits the number of timecode elements:
            1: returns: FF
            2: returns: SS:FF
            3: returns: MM:SS:FF
            4: returns: HH:MM:SS:FF
            0: returns an auto-cropped timecode with no zero elements
        subsecond_type: String, determines the format of the final element of the timecode:
            'miliseconds': subseconds will be divided by 100
            'frames': subseconds will be divided by the current fps
        mode: return mode, if 'string', will return a string timecode, if other, will return a list of integers

    Returns: A string timecode"""

    #ensure the levels value is sane
    if levels > 4:
        levels = 4

    #set the sub second divisor type
    if subsecond_type == 'frames':
        subsecond_divisor = fps
    else:
        subsecond_divisor = 100

    #check for negative values
    if frame < 0:
        negative = True
        frame = abs(frame)
    else:
        negative = False

    #calculate divisions, starting at largest and taking the remainder of each to calculate the next smaller
    total_hours = math.modf(float(frame)/fps/60.0/60.0)
    total_minutes = math.modf(total_hours[0] * 60)
    remaining_seconds = math.modf(total_minutes[0] * 60)
    hours = int(total_hours[1])
    minutes = int(total_minutes[1])
    seconds = int(remaining_seconds[1])
    subseconds = int(round(remaining_seconds[0] * subsecond_divisor))

    if mode != 'string':
        return [hours, minutes, seconds, subseconds]
    else:
        hours_text = str(hours).zfill(2)
        minutes_text = str(minutes).zfill(2)
        seconds_text = str(seconds).zfill(2)
        subseconds_text = str(subseconds).zfill(2)

        #format and return the time value
        time_text = subseconds_text
        if levels > 1 or (levels == 0 and seconds > 0):
            time_text = seconds_text+'.'+time_text
        if levels > 2 or (levels == 0 and minutes > 0):
            time_text = minutes_text+':'+time_text
        if levels > 3 or (levels == 0 and hours > 0):
            time_text = hours_text+':'+time_text
        if negative:
            time_text = '-'+time_text
        return time_text


text = ''
fps = get_fps()
markers = bpy.context.scene.timeline_markers
new_text = bpy.data.texts.new('Timeline Marker Export')
for marker in markers:
    marker_timecode = timecode_from_frames(marker.frame - 1, fps, levels=4)
    line = marker_timecode+' : '+marker.name+'\n'
    new_text.write(line)
