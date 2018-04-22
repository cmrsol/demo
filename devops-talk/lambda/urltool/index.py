index_page = """
<html lang="en">
  <head>
    <script type="text/javascript">
       function postData() {
          var thingy;
          var r;
          var wrk;
          var endpoint;

          console.log('postData(): called');
          document.getElementById('message').innerHTML = 'message: waiting';
          if (window.XMLHttpRequest) {
              xhttp=new XMLHttpRequest();
              console.log('postData(): able to POST with modern methods');
          } else {
              console.log('postData(): is not right');
              return;
          }

          xhttp.onreadystatechange = function() {
              if (xhttp.readyState == 4 && xhttp.status == 200) {
                  console.log('response text: ' + xhttp.responseText);
                  r = JSON.parse(xhttp.responseText);
                  the_new_url = window.location.href + '/url/' + r.key
                  the_stuff = '<a href="' + the_new_url + '"'
                  the_stuff = the_stuff + ' target="' + r.key + '">'
                  the_stuff = the_stuff + the_new_url + '</a>'
                  document.getElementById('message').innerHTML = 'saved URL: ' + the_stuff;
              }
          };


          thingy = new Object();
          endpoint = window.location.href + '/url'
          thingy.url = document.getElementById('url').value
          theData = JSON.stringify(thingy);
          xhttp.open('POST', endpoint, true);
          xhttp.setRequestHeader('Content-type', 'application/json');
          xhttp.send(theData);
       }
    </script>
  </head>
  <body>
    <div id="message">message: nothing to report yet</div><br>
    <form id="the_form">
       <table>
         <tr>
           <td align="right">
           <strong>URL:</strong>
           </td>
           <td><input type="text" id="url" size="64" /></td>
         </tr>
       </table>
       <p> <button type="button" onclick="postData();">Record URL</button> </p>
    </form>
    <p>v0.2</p>
  </body>
</html>
"""
