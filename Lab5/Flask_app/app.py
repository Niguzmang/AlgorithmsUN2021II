<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        <meta charset="utf-8">
        <title>app.py : /home/jcallejas/mysite/Flask-Pdf-Splitter--master/app.py : Editor : jcallejas : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="app.py : /home/jcallejas/mysite/Flask-Pdf-Splitter--master/app.py : Editor : jcallejas : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/output.4f6d24cb0eef.css" type="text/css" media="screen">
        <link rel="stylesheet" href="/static/CACHE/css/output.c184c0fc7128.css" type="text/css"><link rel="stylesheet" href="/static/CACHE/css/output.06c264d5e5d4.css" type="text/css" media="screen">

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "f8PHC0jDGQQhtViU5B268euHJDCp5EBUbxBdf0lyZear9tETrdArac2BD52yrDbQ";
        </script>
        <script src="/static/CACHE/js/output.9912b9c89b96.js"></script>
        

        <script src="/static/CACHE/js/output.d43af9b0891b.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/jcallejas/files/home/jcallejas/mysite/Flask-Pdf-Splitter--master/app.py",
          check_hash: "/user/jcallejas/files/home/jcallejas/mysite/Flask-Pdf-Splitter--master/app.py",
          update_editor_mode_preference: "/user/jcallejas/account/update_editor_mode_preference",
          console_api: "/api/v0/user/jcallejas/consoles/",
        });
        var filename = "/home/jcallejas/mysite/Flask\u002DPdf\u002DSplitter\u002D\u002Dmaster/app.py";
        var hash = "94ead6963b7b8777212a96c22e281a85";
        var interpreter = "python3.9";

        
            Anywhere.Editor.InitializeAce(ace, Anywhere.urls, filename, hash, interpreter, "pythonanywhere.com");
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/jcallejas/files/sharing/",
            csrfToken: "f8PHC0jDGQQhtViU5B268euHJDCp5EBUbxBdf0lyZear9tETrdArac2BD52yrDbQ",
            path: "/home/jcallejas/mysite/Flask\u002DPdf\u002DSplitter\u002D\u002Dmaster/app.py"
          }
        );

      });
    </script>

        

    </head>

     <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/jcallejas/files/">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/jcallejas/files/home">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/jcallejas/files/home/jcallejas">jcallejas</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/jcallejas/files/home/jcallejas/mysite">mysite</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/jcallejas/files/home/jcallejas/mysite/Flask-Pdf-Splitter--master">Flask-Pdf-Splitter--master</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">app.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
          
            <form class="reload_web_app" style="display: flex" method="POST" action="/user/jcallejas/webapps/jcallejas.pythonanywhere.com/reload">
              <button class="btn btn-default" type="submit" title="Reload jcallejas.pythonanywhere.com">
                <i class="glyphicon glyphicon-refresh"></i>
              </button>
              <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
              <div style="display: none; clear: both;" class="alert alert-danger error_message generic_error">
                There was a problem. If this keeps happening, please <a href="" class="feedback_link">send us feedback</a>.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message slow_startup_error">
                Your webapp took a long time to reload. It probably reloaded, but we were unable to check it.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message virtualenv_error">
                There is a problem with your virtualenv setup. Look at the <b>virtualenv</b> section on the web app tab for details.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message cname_error">
                There is a problem with your DNS configuration. Take a look at the <b>DNS setup</b> section on the web app tab for details.
              </div>
            </form>
          
        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  <li class=""><a id="id_dashboard_link" href="/user/jcallejas/">Dashboard</a></li>
  <li class=""><a id="id_consoles_link" href="/user/jcallejas/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/jcallejas/files/home/jcallejas">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/jcallejas/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/jcallejas/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/jcallejas/databases/">Databases</a></li>


        <li class=""><a href="" class="feedback_link">Send feedback</a></li>
<li class=""><a href="/forums/" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" class="help_link">Help</a></li>
<li class=""><a href="https://blog.pythonanywhere.com/" class="blog_link">Blog</a></li>

  
  <li class=""><a href="/user/jcallejas/account/" class="account_link">Account</a></li>
  <li class="">
    <form action="/logout/" method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="f8PHC0jDGQQhtViU5B268euHJDCp5EBUbxBdf0lyZear9tETrdArac2BD52yrDbQ">
      <button type="submit" class="btn-link logout_link">Log out</button>
    </form>
  </li>


      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">from flask import *
import pdfsplitter
app=Flask(__name__)


@app.route(&quot;/&quot;)
def upload():
    return render_template(&quot;file_upload.html&quot;)


@app.route(&quot;/success&quot;,methods=[&quot;POST&quot;])
def success():
    success.start_page=int(request.form[&#39;start&#39;])
    success.end_page=int(request.form[&#39;end&#39;])
    f=request.files[&#39;file&#39;]
    success.file_name=f.filename
    f.save(success.file_name)
    return render_template(&quot;success.html&quot;,start=success.start_page,
                           end=success.end_page,name=success.file_name)

@app.route(&quot;/convert&quot;)
def cropper():
    pdfsplitter.cropper(success.start_page,success.end_page,success.file_name)
    return render_template(&quot;download.html&quot;)



@app.route(&quot;/download&quot;)
def download():
    filename=success.file_name.split(&quot;.&quot;)[0]+&quot;cropped.pdf&quot;
    return send_file(filename,as_attachment=True)


if __name__ == &quot;__main__&quot;:
    app.run(debug=True)
</div>
      

      <div id="id_ide_console">
        
          <div id="id_ide_console_pane_buttons">
            <center>
              
                <button class="btn btn-large btn-info run_button" title="Save &amp; Run (Ctrl + R)">&gt;&gt;&gt; Run this file</button>
                <button class="btn btn-large btn-info bash_console_here" title="Start a Bash console in this folder">$ Bash console here</button>
              
            </center>
          </div>
          <iframe style="display: none" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
          <div style="display: none;" class="console_limit_reached">
            <div class="container">
    <div class="row">
        <div class="col-md-5 col-md-offset-3 well">
            <h1>Console limit reached :-/</h1>

            <p>
            With your current PythonAnywhere account you can have up to
            2 consoles.  You can
            have more if you
            <a href="/user/jcallejas/account/">upgrade your account</a>!

            <p>
            Alternatively, if you don't feel like paying us more money, you
            can <a href="/user/jcallejas/consoles/">kill some consoles on your Consoles page</a>.
        </div>
    </div>
</div>


          </div>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" style="display: none">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_rate_limit_error" style="display: none">
        Sorry, we have had to rate-limit your feedback sending.<br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_success" style="display: none">
        Thanks for the feedback! Our tireless devs will get back to you soon.
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
    <div id="id_feedback_dialog_only_close_button" style="display: none">
        <button class="btn btn-primary" id="id_feedback_dialog_close_button">Close</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
