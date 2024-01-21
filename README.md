# Repository for AI4Phys hackathon

Below organization details, data access, and group splitting.


## Organization

Hacks Mon & Tue 10.15-16.45, optionally Wed afternoon.
Note: Tue at [U-Tokyo DLX Design Lab](https://www.google.com/maps/place/U-Tokyo+DLX+Design+Lab+-+Kashiwa/@35.8935037,139.9432189,17z/data=!3m1!4b1!4m6!3m5!1s0x60189d08be0138ad:0x711bcecd5a9d7c9e!8m2!3d35.8934994!4d139.9457938!16s%2Fg%2F11ryljy207?entry=ttu).
Hack summary Fri 16.15-16.45.


## Using the data

Data accessible in the Google drive:
[https://drive.google.com/drive/u/1/folders/13ySEme-B8XDMYgTZ8\_rVpMarRUUGYbTw](https://drive.google.com/drive/u/1/folders/13ySEme-B8XDMYgTZ8_rVpMarRUUGYbTw)

We suggest you use Google colab for the hack. 
It is most straightforward to directly work with the above Google drive from colab,
since the files don't need to leave Google's servers in that case.
The way I figured out how to do this is as follows (there might be a better method):
1. open the above Google drive.
2. right-click on the file or folder you need.
3. click "Organize" -> "Add shortcut".
4. in "All locations", choose "My Drive" and click "Add".
5. in the colab instance, open the "Files" explorer on the left.
6. click "Mount Drive" icon.
7. you should be able to see the file now.
   To switch the colab working directory to your drive, type:
   ``cd "/content/drive/MyDrive/"``


## Available data sets

1. **SDSS spectra** (thanks to *Hideki Tanimura*)  
   Some galaxy spectra from the Sloan Digital Sky Survey.  
   loading: [Read\_sdss.ipynb](Read_sdss.ipynb)  
   data: ``sdss_galaxy_spec.hdf5``
2. **Gaia** (thanks to *Hideki Tanimura*)  
   Spectra from the Gaia satellite.  
   loading: [Read\_gaia.ipynb](Read_gaia.ipynb)  
   data: ``gaia_star_spec.hdf5``
3. **HSC Y1 convergence maps and summary statistics** (thanks to *Joaquin Armijo*)  
   Real and simulated weak lensing convergence maps for HSC Y1.  
   Also available are some summary statistics for these maps.  
   [Marques et al 2023](https://ui.adsabs.harvard.edu/abs/2024MNRAS.tmp...91M/abstract)  
   loading: [HSC\_NG\_ConvergenceMaps.ipynb](HSC_NG_ConvergenceMaps.ipynb)  
   data: ``HSC_NG/``
4. **JWST COSMOS web galaxy images** (thanks to *Xuheng Ding*)  
   A sample of galaxy images from JWST.  
   loading: [read\_data\_jwst\_cosmos\_web.py](read_data_jwst_cosmos_web.py)  
   data: ``COSMOS_web_galaxies.zip``
5. **HSC images** (thanks to *Chris Nagele*)  
   A sample of galaxy images from HSC.  
   [Nagele et al 2023](https://ui.adsabs.harvard.edu/abs/2023ApJ...947...30N/abstract)  
   loading: [QSO\_SFG\_example.py](QSO_SFG_example.py)  
   data: ``QSO_SFG_data.npy``
6. **SIMBIG galaxy catalogs** (thanks to *Bruno Regaldo*)  
   Real and simulated data for SDSS BOSS.  
   Note that the files require [nbodykit](https://nbodykit.readthedocs.io) and [bigfile](https://github.com/rainwoodman/bigfile).  
   [Hahn et al 2023a](https://ui.adsabs.harvard.edu/abs/2023PNAS..12018810H/abstract),
   [Hahn et al 2023b](https://ui.adsabs.harvard.edu/abs/2023JCAP...04..010H/abstract)  
   loading: [simbig\_code](simbig_code)  
   data: ``simbig_sample.zip``
7. **CAMELS 2D multifield data** (thanks to *Francisco Villaescusa-Navarro*)
   Images of 25 Mpc/h simulated boxes from the [CAMELS](https://camels.readthedocs.io) project.  
   [data website](https://camels-multifield-dataset.readthedocs.io),
   [Villaescusa-Navarro et al 2022](https://ui.adsabs.harvard.edu/abs/2022ApJS..259...61V/abstract)  
   loading: TODO  
   data: TODO  


## Hack groups

Please find group assignment below.
For each group, we suggest you work on one out of three data sets
(this is to encourage some variety in the topics people choose).
If you absolutely want to work on a data set that is not listed, this is a free country.


### Group A
suggested topics: SDSS spectra (1), Gaia (2), SIMBIG (6)
- Tochon, Guillaume
- Tanimura, Hideki 
- Ohana, Ruben     
- Leyde, Konstantin
- Dixit, Vaibhav   
- Li, Zhuohan      

### Group B
suggested topics: Gaia(2), SDSS spectra (1)
- Zadrożny, Adam  
- Golkar, Siavash 
- Novaes, Camila  
- Tanaka, Takumi  
- Alexandre, Adam 
- Hehir, Thomas   

### Group C
suggested topics: Gaia (2), HSC convergence (3), SIMBIG (6)
- Shirley, Ho              
- Fromenteau, Sébastien    
- Perez Diaz, Victor Samuel
- Horowitz, Benjamin       
- Craigie, Matt            
- Adrián, Gutiérrez Adame  
- Rukundo Benjamin         

### Group D
suggested topics: Gaia (2), JWST images (4), CAMELS multifield (7)
- Hotokezaka, Kenta    
- Eickenberg, Michael  
- Pettee, Mariel       
- Ferrero, Ismael      
- Tokiwa, Akira        
- Park, Core Francisco 
- Bell, Rianna         

### Group E
suggested topics: SDSS spectra (1), HSC convergence (3), SIMBIG (6)
- Vargas-Magaña, Mariana
- Dawi, Anna            
- Ramachandra, Nesar    
- Cooray, Suchetha      
- Hidayat, Wildan       
- Birky, Jessica        
- Hilmi, Miftahul       

### Group F
suggested topics: Gaia (2), JWST images (4), SIMBIG (6)
- Shi, Jingjing                  
- Bayer, Adrian                  
- Li, Jennifer                   
- Porter, Fiona                  
- Shi, Claudia                   
- Yoon, Seongwhan                
- Soler Matubaro de Santi, Natalí

### Group G
suggested topics: Gaia (2), HSC convergence (3), CAMELS multifield (7)
- Huertas-Company, Marc         
- McCabe, Michael               
- Onoue, Masafusa               
- Kumar Yadav, Sarvesh          
- Thiele, Leander               
- Henrique Mendes Duarte, Pedro 
- Angeloudi, Eirini             

### Group H
suggested topics: HSC convergence (3), HSC images (5), SIMBIG (6)
- Liu, Jia            
- Bogatskiy, Alexander
- Dan, Jiadong        
- Medvidović, Matija  
- Li, Chester         
- Lahiry, Arnab       

### Group J
suggested topics: JWST images (4), SIMBIG (6), CAMELS multifield (7)
- Li, Yin                 
- Qiu, Tian               
- Yuan, Sihan             
- Wagner-Carena, Sebastian
- Sampson, Matthew        
- Chu, Jiani              
- Breitman, Daniela       

### Group K
suggested topics: HSC convergence (3), SIMBIG (6), CAMELS multifield (7)
- Nishizawa, Atsushi           
- Cheung, Mark                 
- Régaldo-Saint Blancard, Bruno
- Scott, Bryan                 
- James, Sunseri               
- Quaglia, Giulio              
- Aizawa, Kosuke               

### Group L
suggested topics: HSC convergence (3), JWST images (4), HSC images (5)
- Nagamine, Kentaro
- Leopoldo, Sarra  
- Armijo, Joaquin  
- Sharma, Ranbir   
- Darwish, Omar    
- Zhang, Xiaowen   
- Hainje, Connor   

### Group M
suggested topics: SDSS spectra (1), JWST images (4), CAMELS multifield (7)
- Moriwaki, Kana            
- Parker, Liam              
- Jost, Baptiste            
- Lammers, Caleb            
- Matthews, Alice           
- Zhou, Alan Junzhe         
- Gondhalekar, Yash Prashant

### Group N
suggested topics: SDSS spectra (1), HSC convergence (3), JWST images (4)cd "/content/drive/MyDrive/
- Zhao, Jingkun   
- Terao, Kazuhiro 
- Myles, Justin   
- Halson, Marcus  
- Hirashima, Keiya
- Wan, Brian      

