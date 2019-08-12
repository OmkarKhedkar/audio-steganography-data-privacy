#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  May 09, 2019 07:34:36 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+476+129
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 225 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 175 
    vTcl:DefineAlias "$top.fra43" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    radiobutton $site_3_0.rad44 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Radio -variable {} 
    vTcl:DefineAlias "$site_3_0.rad44" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_3_0.rad45 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Radio -variable {} 
    vTcl:DefineAlias "$site_3_0.rad45" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_3_0.rad46 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Radio -variable {} 
    vTcl:DefineAlias "$site_3_0.rad46" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $site_3_0.rad47 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Radio -variable {} 
    vTcl:DefineAlias "$site_3_0.rad47" "Radiobutton4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but43 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Button 
    vTcl:DefineAlias "$site_3_0.but43" "Button1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.rad44 \
        -in $site_3_0 -x 30 -y 20 -width 58 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad45 \
        -in $site_3_0 -x 30 -y 60 -anchor nw -bordermode ignore 
    place $site_3_0.rad46 \
        -in $site_3_0 -x 30 -y 100 -anchor nw -bordermode ignore 
    place $site_3_0.rad47 \
        -in $site_3_0 -x 30 -y 140 -width 58 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but43 \
        -in $site_3_0 -x 60 -y 180 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 160 -y 70 -width 175 -relwidth 0 -height 225 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

