def parse_a(div):
  a_bulk_space = div.split(' ')
  start = 0
  needed_link = ''
  title_mass_get = div.split('</span>')
  title_mass = title_mass_get[0].split('><span>')
  title = title_mass[1]
  #print(title)
  while start < len(a_bulk_space):
    if ('href' in a_bulk_space[start]):
      needed_link = a_bulk_space[start]
    start+=1
  return [needed_link.replace('href="','').replace('"',''),title]