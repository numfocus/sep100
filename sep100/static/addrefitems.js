var refitems = {
  "ArXive": "Hello",
               }

function addRefItems() {
  for (refkey in refitems)
  {
    var refval = refitems[refkey];
    var s;
    s = '<div class="refitemname"><a style="font-size: 150%">' + refkey + '</a></div>\n';
    
    document.write(s)
//      <div class="refiteminput"><input type="text" name="doi" size="18" /></div>
//      <div class="refitemtip"><a style="font-size: 90%">DOI number.</a></div>
//      <div class="refitemclear" />
//      <br />
//      <br />
)
  };
};

