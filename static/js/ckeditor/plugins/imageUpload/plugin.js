CKEDITOR.plugins.add( 'imageUpload',{   
    init : function( editor ){      
 
  		var pluginName = 'imageUpload'; 
		CKEDITOR.dialog.add(pluginName, this.path + 'dialogs/imageUpload.js');   
        editor.addCommand(pluginName, new CKEDITOR.dialogCommand(pluginName));   
        editor.ui.addButton( 'imageUpload',   
        {   
                label : '图片',  
                icon: this.path + 'images/images.jpg',
                command : pluginName 
        });   
    },   
    requires : [ 'dialog' ]   
});