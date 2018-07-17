from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Scene(BaseLayoutHierarchyType):

    # annotations
    # -----------
    @property
    def annotations(self):
        """
        The 'annotations' property is a tuple of instances of
        Annotation that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.scene.Annotation
          - A list or tuple of dicts of string/value properties that
            will be passed to the Annotation constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the `text`
                    within the box. Has an effect only if `text`
                    spans more two or more lines (i.e. `text`
                    contains one or more <br> HTML tags) or if an
                    explicit width is set to override the text
                    width.
                arrowcolor
                    Sets the color of the annotation arrow.
                arrowhead
                    Sets the end annotation arrow head style.
                arrowside
                    Sets the annotation arrow head position.
                arrowsize
                    Sets the size of the end annotation arrow head,
                    relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                arrowwidth
                    Sets the width (in px) of annotation arrow
                    line.
                ax
                    Sets the x component of the arrow tail about
                    the arrow head (in pixels).
                ay
                    Sets the y component of the arrow tail about
                    the arrow head (in pixels).
                bgcolor
                    Sets the background color of the annotation.
                bordercolor
                    Sets the color of the border enclosing the
                    annotation `text`.
                borderpad
                    Sets the padding (in px) between the `text` and
                    the enclosing border.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the annotation `text`.
                captureevents
                    Determines whether the annotation text box
                    captures mouse move and click events, or allows
                    those events to pass through to data points in
                    the plot that may be behind the annotation. By
                    default `captureevents` is *false* unless
                    `hovertext` is provided. If you use the event
                    `plotly_clickannotation` without `hovertext`
                    you must explicitly enable `captureevents`.
                font
                    Sets the annotation text font.
                height
                    Sets an explicit height for the text box. null
                    (default) lets the text set the box height.
                    Taller text will be clipped.
                hoverlabel
                    plotly.graph_objs.layout.scene.annotation.Hover
                    label instance or dict with compatible
                    properties
                hovertext
                    Sets text to appear when hovering over this
                    annotation. If omitted or blank, no hover label
                    will appear.
                opacity
                    Sets the opacity of the annotation (text +
                    arrow).
                showarrow
                    Determines whether or not the annotation is
                    drawn with an arrow. If *true*, `text` is
                    placed near the arrow's tail. If *false*,
                    `text` lines up with the `x` and `y` provided.
                standoff
                    Sets a distance, in pixels, to move the end
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
                startarrowhead
                    Sets the start annotation arrow head style.
                startarrowsize
                    Sets the size of the start annotation arrow
                    head, relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                startstandoff
                    Sets a distance, in pixels, to move the start
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
                text
                    Sets the text associated with this annotation.
                    Plotly uses a subset of HTML tags to do things
                    like newline (<br>), bold (<b></b>), italics
                    (<i></i>), hyperlinks (<a href='...'></a>).
                    Tags <em>, <sup>, <sub> <span> are also
                    supported.
                textangle
                    Sets the angle at which the `text` is drawn
                    with respect to the horizontal.
                valign
                    Sets the vertical alignment of the `text`
                    within the box. Has an effect only if an
                    explicit height is set to override the text
                    height.
                visible
                    Determines whether or not this annotation is
                    visible.
                width
                    Sets an explicit width for the text box. null
                    (default) lets the text set the box width.
                    Wider text will be clipped. There is no
                    automatic wrapping; use <br> to start a new
                    line.
                x
                    Sets the annotation's x position.
                xanchor
                    Sets the text box's horizontal position anchor
                    This anchor binds the `x` position to the
                    *left*, *center* or *right* of the annotation.
                    For example, if `x` is set to 1, `xref` to
                    *paper* and `xanchor` to *right* then the
                    right-most portion of the annotation lines up
                    with the right-most edge of the plotting area.
                    If *auto*, the anchor is equivalent to *center*
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                xshift
                    Shifts the position of the whole annotation and
                    arrow to the right (positive) or left
                    (negative) by this many pixels.
                y
                    Sets the annotation's y position.
                yanchor
                    Sets the text box's vertical position anchor
                    This anchor binds the `y` position to the
                    *top*, *middle* or *bottom* of the annotation.
                    For example, if `y` is set to 1, `yref` to
                    *paper* and `yanchor` to *top* then the top-
                    most portion of the annotation lines up with
                    the top-most edge of the plotting area. If
                    *auto*, the anchor is equivalent to *middle*
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                yshift
                    Shifts the position of the whole annotation and
                    arrow up (positive) or down (negative) by this
                    many pixels.
                z
                    Sets the annotation's z position.

        Returns
        -------
        tuple[plotly.graph_objs.layout.scene.Annotation]
        """
        return self['annotations']

    @annotations.setter
    def annotations(self, val):
        self['annotations'] = val

    # aspectmode
    # ----------
    @property
    def aspectmode(self):
        """
        If *cube*, this scene's axes are drawn as a cube, regardless of
        the axes' ranges. If *data*, this scene's axes are drawn in
        proportion with the axes' ranges. If *manual*, this scene's
        axes are drawn in proportion with the input of *aspectratio*
        (the default behavior if *aspectratio* is provided). If *auto*,
        this scene's axes are drawn using the results of *data* except
        when one axis is more than four times the size of the two
        others, where in that case the results of *cube* are used.
    
        The 'aspectmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'cube', 'data', 'manual']

        Returns
        -------
        Any
        """
        return self['aspectmode']

    @aspectmode.setter
    def aspectmode(self, val):
        self['aspectmode'] = val

    # aspectratio
    # -----------
    @property
    def aspectratio(self):
        """
        Sets this scene's axis aspectratio.
    
        The 'aspectratio' property is an instance of Aspectratio
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Aspectratio
          - A dict of string/value properties that will be passed
            to the Aspectratio constructor
    
            Supported dict properties:
                
                x
    
                y
    
                z

        Returns
        -------
        plotly.graph_objs.layout.scene.Aspectratio
        """
        return self['aspectratio']

    @aspectratio.setter
    def aspectratio(self, val):
        self['aspectratio'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # camera
    # ------
    @property
    def camera(self):
        """
        The 'camera' property is an instance of Camera
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Camera
          - A dict of string/value properties that will be passed
            to the Camera constructor
    
            Supported dict properties:
                
                center
                    Sets the (x,y,z) components of the 'center'
                    camera vector This vector determines the
                    translation (x,y,z) space about the center of
                    this scene. By default, there is no such
                    translation.
                eye
                    Sets the (x,y,z) components of the 'eye' camera
                    vector. This vector determines the view point
                    about the origin of this scene.
                up
                    Sets the (x,y,z) components of the 'up' camera
                    vector. This vector determines the up direction
                    of this scene with respect to the page. The
                    default is *{x: 0, y: 0, z: 1}* which means
                    that the z axis points up.

        Returns
        -------
        plotly.graph_objs.layout.scene.Camera
        """
        return self['camera']

    @camera.setter
    def camera(self, val):
        self['camera'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this scene subplot
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this scene subplot .
                x
                    Sets the horizontal domain of this scene
                    subplot (in plot fraction).
                y
                    Sets the vertical domain of this scene subplot
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.layout.scene.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # dragmode
    # --------
    @property
    def dragmode(self):
        """
        Determines the mode of drag interactions for this scene.
    
        The 'dragmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['orbit', 'turntable', 'zoom', 'pan', False]

        Returns
        -------
        Any
        """
        return self['dragmode']

    @dragmode.setter
    def dragmode(self, val):
        self['dragmode'] = val

    # hovermode
    # ---------
    @property
    def hovermode(self):
        """
        Determines the mode of hover interactions for this scene.
    
        The 'hovermode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['closest', False]

        Returns
        -------
        Any
        """
        return self['hovermode']

    @hovermode.setter
    def hovermode(self, val):
        self['hovermode'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        The 'xaxis' property is an instance of XAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.XAxis
          - A dict of string/value properties that will be passed
            to the XAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to *false*.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to *array*. Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    *trace*, which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to *array*
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    *trace* mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If *true*, the axis lines are mirrored.
                    If *ticks*, the axis lines and ticks are
                    mirrored. If *false*, mirroring is disable. If
                    *all*, axis lines are mirrored on all shared-
                    axes subplots. If *allticks*, axis lines and
                    ticks are mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                range
                    Sets the range of this axis. If the axis `type`
                    is *log*, then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is *date*, it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is *category*, it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If *normal*, the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If *nonnegative*, the range is non-
                    negative, regardless of the input data.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If *true*, the grid lines are drawn at every
                    tick mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.layout.scene.xaxis.Tickformat
                    stop instance or dict with compatible
                    properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If *true*, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.XAxis
        """
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        The 'yaxis' property is an instance of YAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.YAxis
          - A dict of string/value properties that will be passed
            to the YAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to *false*.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to *array*. Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    *trace*, which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to *array*
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    *trace* mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If *true*, the axis lines are mirrored.
                    If *ticks*, the axis lines and ticks are
                    mirrored. If *false*, mirroring is disable. If
                    *all*, axis lines are mirrored on all shared-
                    axes subplots. If *allticks*, axis lines and
                    ticks are mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                range
                    Sets the range of this axis. If the axis `type`
                    is *log*, then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is *date*, it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is *category*, it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If *normal*, the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If *nonnegative*, the range is non-
                    negative, regardless of the input data.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If *true*, the grid lines are drawn at every
                    tick mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.layout.scene.yaxis.Tickformat
                    stop instance or dict with compatible
                    properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If *true*, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.YAxis
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # zaxis
    # -----
    @property
    def zaxis(self):
        """
        The 'zaxis' property is an instance of ZAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.ZAxis
          - A dict of string/value properties that will be passed
            to the ZAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to *false*.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to *array*. Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    *trace*, which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to *array*
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    *trace* mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If *true*, the axis lines are mirrored.
                    If *ticks*, the axis lines and ticks are
                    mirrored. If *false*, mirroring is disable. If
                    *all*, axis lines are mirrored on all shared-
                    axes subplots. If *allticks*, axis lines and
                    ticks are mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                range
                    Sets the range of this axis. If the axis `type`
                    is *log*, then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is *date*, it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is *category*, it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If *normal*, the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If *nonnegative*, the range is non-
                    negative, regardless of the input data.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If *true*, the grid lines are drawn at every
                    tick mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.layout.scene.zaxis.Tickformat
                    stop instance or dict with compatible
                    properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If *true*, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.ZAxis
        """
        return self['zaxis']

    @zaxis.setter
    def zaxis(self, val):
        self['zaxis'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        annotations
            plotly.graph_objs.layout.scene.Annotation instance or
            dict with compatible properties
        aspectmode
            If *cube*, this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If *data*, this scene's
            axes are drawn in proportion with the axes' ranges. If
            *manual*, this scene's axes are drawn in proportion
            with the input of *aspectratio* (the default behavior
            if *aspectratio* is provided). If *auto*, this scene's
            axes are drawn using the results of *data* except when
            one axis is more than four times the size of the two
            others, where in that case the results of *cube* are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            plotly.graph_objs.layout.scene.Camera instance or dict
            with compatible properties
        domain
            plotly.graph_objs.layout.scene.Domain instance or dict
            with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        xaxis
            plotly.graph_objs.layout.scene.XAxis instance or dict
            with compatible properties
        yaxis
            plotly.graph_objs.layout.scene.YAxis instance or dict
            with compatible properties
        zaxis
            plotly.graph_objs.layout.scene.ZAxis instance or dict
            with compatible properties
        """

    def __init__(
        self,
        arg=None,
        annotations=None,
        aspectmode=None,
        aspectratio=None,
        bgcolor=None,
        camera=None,
        domain=None,
        dragmode=None,
        hovermode=None,
        xaxis=None,
        yaxis=None,
        zaxis=None,
        **kwargs
    ):
        """
        Construct a new Scene object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Scene
        annotations
            plotly.graph_objs.layout.scene.Annotation instance or
            dict with compatible properties
        aspectmode
            If *cube*, this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If *data*, this scene's
            axes are drawn in proportion with the axes' ranges. If
            *manual*, this scene's axes are drawn in proportion
            with the input of *aspectratio* (the default behavior
            if *aspectratio* is provided). If *auto*, this scene's
            axes are drawn using the results of *data* except when
            one axis is more than four times the size of the two
            others, where in that case the results of *cube* are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            plotly.graph_objs.layout.scene.Camera instance or dict
            with compatible properties
        domain
            plotly.graph_objs.layout.scene.Domain instance or dict
            with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        xaxis
            plotly.graph_objs.layout.scene.XAxis instance or dict
            with compatible properties
        yaxis
            plotly.graph_objs.layout.scene.YAxis instance or dict
            with compatible properties
        zaxis
            plotly.graph_objs.layout.scene.ZAxis instance or dict
            with compatible properties

        Returns
        -------
        Scene
        """
        super(Scene, self).__init__('scene')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Scene 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Scene"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (scene as v_scene)

        # Initialize validators
        # ---------------------
        self._validators['annotations'] = v_scene.AnnotationsValidator()
        self._validators['aspectmode'] = v_scene.AspectmodeValidator()
        self._validators['aspectratio'] = v_scene.AspectratioValidator()
        self._validators['bgcolor'] = v_scene.BgcolorValidator()
        self._validators['camera'] = v_scene.CameraValidator()
        self._validators['domain'] = v_scene.DomainValidator()
        self._validators['dragmode'] = v_scene.DragmodeValidator()
        self._validators['hovermode'] = v_scene.HovermodeValidator()
        self._validators['xaxis'] = v_scene.XAxisValidator()
        self._validators['yaxis'] = v_scene.YAxisValidator()
        self._validators['zaxis'] = v_scene.ZAxisValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('annotations', None)
        self.annotations = annotations if annotations is not None else _v
        _v = arg.pop('aspectmode', None)
        self.aspectmode = aspectmode if aspectmode is not None else _v
        _v = arg.pop('aspectratio', None)
        self.aspectratio = aspectratio if aspectratio is not None else _v
        _v = arg.pop('bgcolor', None)
        self.bgcolor = bgcolor if bgcolor is not None else _v
        _v = arg.pop('camera', None)
        self.camera = camera if camera is not None else _v
        _v = arg.pop('domain', None)
        self.domain = domain if domain is not None else _v
        _v = arg.pop('dragmode', None)
        self.dragmode = dragmode if dragmode is not None else _v
        _v = arg.pop('hovermode', None)
        self.hovermode = hovermode if hovermode is not None else _v
        _v = arg.pop('xaxis', None)
        self.xaxis = xaxis if xaxis is not None else _v
        _v = arg.pop('yaxis', None)
        self.yaxis = yaxis if yaxis is not None else _v
        _v = arg.pop('zaxis', None)
        self.zaxis = zaxis if zaxis is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))