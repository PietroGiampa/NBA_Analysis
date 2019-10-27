from GetData import ExportShootingToText
from GetData import FormatData

player = 'jamesle01'
year = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
for k in range(15):    
    ExportShootingToText(player, year[k])
    FormatData(player, year[k])
