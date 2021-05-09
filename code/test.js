const { createClient } = require('@supabase/supabase-js')
console.log('test')

const supabase = createClient(
  'https://bktrqpzyfcfkxrcupqqa.supabase.co',
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYyMDQ5MDQwNCwiZXhwIjoxOTM2MDY2NDA0fQ.k2epLv58prooz7qaeKw9GrZW5DuyDHR-vQ6MkMreoJ8'
)

const main = async () => {
  let { data: aaaaaaa, error } = await supabase
    .from('aaaaaaa')
    .select('*')

  if (error) {
    console.log(error)
    return
  }

  console.log(aaaaaaa)
}
main()