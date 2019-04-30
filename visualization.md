

## Collection

* http://www.popodv.com/awesome.html#7 
* course 
  * https://courses.engr.illinois.edu/cs199205/sp2017/index.php 



[Calculus on Computational Graphs: Backpropagation](http://colah.github.io/posts/2015-08-Backprop/) 

## Math

* interactive mathematical visualizations built using [MathBox](https://gitgud.io/unconed/mathbox):
     * examples [mathbox](http://stemkoski.github.io/MathBox/index.html) 

     * collection [GitHub](https://github.com/stemkoski/stemkoski.github.com) 

     * python example 

       * [notebook](https://www.google.com/url?q=https%3A%2F%2Fnbviewer.jupyter.org%2Fgithub%2Fznah%2Fmathbox%2Fblob%2Fjupyter%2Fexamples%2Fnotebooks%2Fmathbox.ipynb%3Fflush_cache%3Dtrue&sa=D&sntz=1&usg=AFQjCNEXDxlAQCxYkPmCMu0tsFWAAHux0A) that shows how one can integrate MathBox plots into Jupyter and feed them data from Python backend. WebGL supporting browser and a decent GPU required.

         > [MathBox2](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Funconed%2Fmathbox&sa=D&sntz=1&usg=AFQjCNGQHiJN4sMsYAzj0EC-BSwi9AAMmQ) is an amazing visualization library created by [Steven Wittens](http://acko.net/). This is a very promising project, containing some really interesting ideas. 








## Bokeh

* example 
  * [Visualization using Bokeh](https://www.kaggle.com/rishabhzn200/visualization-using-bokeh) 
* bokeh.io
  * `curdoc`()[[source\]](https://bokeh.pydata.org/en/latest/_modules/bokeh/io/doc.html#curdoc)[¶](https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.curdoc) 
  * `install_notebook_hook`(*notebook_type*, *load*, *show_doc*, *show_app*, *overwrite=False*)[[source\]](https://bokeh.pydata.org/en/latest/_modules/bokeh/io/notebook.html#install_notebook_hook)[¶](https://bokeh.pydata.org/en/latest/docs/reference/io.html#bokeh.io.install_notebook_hook) 
* [bokeh-notebooks](https://github.com/bokeh/bokeh-notebooks)/[tutorial](https://github.com/bokeh/bokeh-notebooks/tree/master/tutorial)/ 
* [Running a Bokeh Server](https://bokeh.pydata.org/en/latest/docs/user_guide/server.html) 



### bugs

* AttributeError: 'Figure' object has no attribute 'hover' 

  * situation

    * `p.hover.tooltips = []`

    * ```
      bokeh.__version__ : '0.12.13'
      ```

  * solution 

    * `p.select(HoverTool).tooltips =`
    * [Possible update in bokeh is causing a strange generator bug](https://stackoverflow.com/questions/35411416/possible-update-in-bokeh-is-causing-a-strange-generator-bug) 
    * [Python Bokeh HoverTool formatters error: “unexpected attribute 'formatters' to HoverTool”](https://stackoverflow.com/questions/45855928/python-bokeh-hovertool-formatters-error-unexpected-attribute-formatters-to-h)

  * 







## Geo_python

* [Distance Calculator in Python ](<http://129.89.35.212/uKnow>)
  * 
* geo_spatial 
  * <https://drive.google.com/file/d/11bYwo7eaUq3ZXTitoiSlA8tXf7fBliME/view?usp=sharing>
  * [jupyter notebook](https://github.com/benryder1988/Spatial-Workshop) 
* [geopython](https://github.com/urschrei/Geopython) 
* [GeoPython - AutoGIS ](https://automating-gis-processes.github.io/2016/index.html): a geo python document for all phases
  *  accessibility: https://automating-gis-processes.github.io/2016/Lesson5-interactive-map-bokeh.html
* [geocoder](https://geocoder.readthedocs.io/) :  an API that returns LAT and Lng of points
* [AccessViz](https://automating-gis-processes.github.io/2016/Final-assignment.html#accessviz) which is a GIS-tool that can visualize and compare travel times by different travel modes in Helsinki Region. 
* [Folium](https://github.com/python-visualization/folium) that makes it possible visualize data that’s been manipulated in Python on an interactive Leaflet map.

 