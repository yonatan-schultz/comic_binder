# comic_binder
A simple python script that combines multiple cbr cbz files into a single collection. 

 Welcome to Comic Binder! It is a simple Python script that zips up multiple cbr and cbz files into a single zip file readable by PerfectViewer or other comic readers. 
 It is useful for finished series or mini-series that you've collected in individual issues and would like to roll up into a single file.
 For now, simply drop it into the folder that contains the comic files and let it run. It will:
 1. Extract all files
 2. Zip them together into a cbz file
 3. Delete all individual cbr and cbz files
 
 When it's done you'll be left with a single .cbz file named after the folder that you are currently in. It expects a file structure of:


 My Comic Collection  
 --------Series 1  
 -------------Issue 1  
 -------------Issue 2  
 -------------Issue 3  
 --------Series 2  
 -------------Issue 1  
 -------------Issue 2  
 -------------Issue 3  
