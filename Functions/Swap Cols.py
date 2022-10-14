# author  :Mohamed Tarek


def swap_col(startups,col1,col2):
  data = list(startups.columns)
  index_rom,index_profit = data.index("ROMS"),data.index("profit")
  data[index_rom],data[index_profit] = data[index_profit],data[index_rom]
  startups = startups[data]
  return startups

startups = swap_col(startups,"col1","col2")





