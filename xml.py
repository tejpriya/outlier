from xml.etree import ElementTree as ET
def convert_xml_files(myroot_dir,txt_dir):
   
    for root, dirs, files in os.walk(myroot_dir):
        for filename in files:
            if filename.endswith('.xml'):
                xml_path = os.path.join(root, filename)
                txt_path = os.path.join(txt_dir, os.path.splitext(filename)[0] + '.txt')
                                
                # Load the XML file and extract the text
                tree = ET.parse(xml_path)
                xml_text = ET.tostring(tree.getroot(), encoding='unicode', method='text')
                
                # Save the text to a TXT file
                with open(txt_path, 'w') as f:
                    f.write(xml_text)

def xmt(request):
    if request.method == 'POST':
        form = xmtx(request.POST)
        if form.is_valid():
            myroot_dir = form.cleaned_data['myroot_dir']
            txt_dir = form.cleaned_data['txt_dir']
            # Convert all XML files in the root directory and its subdirectories to TXT
            convert_xml_files(myroot_dir,txt_dir)
            form.save() 
            # Display a success message
            return redirect('xmtx_url')
            # return redirect('success_url')
    else:
          form = xmtx()
    
    context = {'form': form}
    return render(request, 'templates/dms/xmt.html', context)