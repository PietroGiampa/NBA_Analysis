#####################################################
## Define Function for Shot Calculations           ##
#####################################################
## Pietro Giampa, August 2019                      ##
#####################################################
import numpy as np

####################################
# List of Functions:
#
# 1) PainfShot(x,y)
# 2) FreeThrow(x,y)
# 3) LowPostLeft(x,y)
# 4) LowPostRight(x,y)
# 5) Corner3Left(x,y)
# 6) Corner3Right(x,y)
# 7) LeftTop3(x,y)
# 8) RightTop3(x,y)
# 9) CenterTop3(x,y)
# 10) MidRangeLeft(x,y)
# 11) MidRangeRight(x,y)
# 12) MidRangeCenter(x,y)
####################################

## Paint Shot ##
ps_x_low = -60
ps_x_high = 60
ps_y_low = -47.5
ps_y_high = 100.0
## Free-Throw ##
ft_x_low = -80
ft_x_high = 80
ps_y_low = 133.5
ps_y_high = 153.5
## Low Post Left ##
lbl_x_low = -60
lbl_x_high = -100
lbl_y_low = -47.5
lbl_y_high = 100.0
## Low Post Right ##
lbr_x_low = 60
lbr_x_high = 100
lbr_y_low = -47.5
lbr_y_high = 100.0
## Mid Range Top Left ##
mrtl_x_low = -100
mrtl_y_low = 92.5
## Mid Range Top Right ##
mrtr_x_low = 100
mrtr_y_low = 92.5
## Mid Range Top Center ##
mrtc_x_low = -100
mrtc_x_high = 100
mrtc_y_low = 153
## Mid Range Low Left ##
mrll_x_low = -100
mrll_x_high = -220
mrll_y_low = -47.5
mrll_y_high = 92.5
## Mid Range Low Left ##
mrlr_x_low = 100
mrlr_x_high = 220
mrlr_y_low = -47.5
mrlr_y_high = 92.5
## Corner-3 Left ##
c3l_x_low = -220
c3l_y_low = -47.5
c3l_y_high = 92.5
## Corner-3 Right ##
c3r_x_low = 220
c3r_y_low = -47.5
c3r_y_high = 92.5
## Left-Top-3 ##
lt3_x_low = -100
lt3_y_low = 92.5
## Right-Top-3 ##
rt3_x_low = 100
rt3_y_low = 92.5
## Center-Top-3 ##
ct3_x_low = -100
ct3_x_high = 100
ct3_y_low = 92.5
## 3-Point ##
rad3 = 239

################################
#          Paint Shot          #
################################
def PaintShot(x, y):
    ps = False
    if x<=ps_x_high and x>=ps_x_low and y>ps_y_low and y<ps_y_high:
        ps = True
    return ps

################################
#          Free Throw          #
################################
def FreeThrow(x, y):
    ft = False
    if x<=ft_x_high and x>=ft_x_low and y>ft_y_low and y<ft_y_high:
        ft = True
    return ft

################################
#        Low Post Left         #
################################
def LowPostLeft(x, y):
    lpl = False
    if x<=lbl_x_high and x>=lbl_x_low and y>lbl_y_low and y<lbl_y_high:
        lbl = True
    return lbl

################################
#        Low Post Left         #
################################
def LowPostRight(x, y):
    lpr = False
    if x<=lbr_x_high and x>=lbr_x_low and y>lbr_y_low and y<lbr_y_high:
        lbr = True
    return lbr

################################
#        Corner-3 Left         #
################################
def Corner3Left(x, y):
    c3l = False
    if x<c3l_x_low and y>c3l_y_low and y<c3l_y_high:
        c3l = True
    return c3l

################################
#        Corner-3 Left         #
################################
def Corner3Right(x, y):
    c3r = False
    if x>c3r_x_low and y>c3r_y_low and y<c3r_y_high:
        c3r = True
    return c3r

################################
#        Left-Top-Three        #   
################################
def LeftTop3(x, y):
    tl3 = False
    radius = np.sqrt(x*x + y*y)
    if x<lt3_x_low and y>lt3_y_low and radius>=rad3:
        tl3 = True
    return tl3

################################
#       Right-Top-Three        #
################################
def RightTop3(x, y):
    rl3 = False
    radius = np.sqrt(x*x + y*y)
    if x>rt3_x_low and y>rt3_y_low and radius>=rad3:
        rl3 = True
    return rl3

################################
#       Center-Top-Three       #
################################
def CenterTop3(x, y):
    cl3 = False
    radius = np.sqrt(x*x + y*y)
    if x>=ct3_x_low and x<=ct3_x_high and radius>=rad3:
        cl3 = True
    return cl3

################################
#      Mid-Range Top Left      #
################################
def MidRangeTopLeft(x, y):
    mrtl = False
    radius = np.sqrt(x*x + y*y)
    if x<=mrtl_x_low and y>=mrtl_y_low and radius<=rad3:
        mrtl = True
    return mrtl

################################
#      Mid-Range Top Left      #
################################
def MidRangeTopRight(x, y):
    mrtr = False
    radius = np.sqrt(x*x + y*y)
    if x<=mrtr_x_low and y>=mrtr_y_low and radius<=rad3:
        mrtr = True
    return mrtr

