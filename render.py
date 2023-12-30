import vtk


def renderer(iso_value):
    colors = vtk.vtkNamedColors()

    # Constants
    DICOM_DIR = 'ct' 
    ISO_VAL = iso_value

    volume = vtk.vtkImageData()
    if DICOM_DIR is None:
        pass

    else:
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(DICOM_DIR)
        reader.Update()
        volume.DeepCopy(reader.GetOutput())

    surface = vtk.vtkMarchingCubes()
    surface.SetInputData(volume)
    surface.ComputeNormalsOn()
    surface.SetValue(0, ISO_VAL)

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(colors.GetColor3d('DarkSlateGray'))

    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetWindowName('MarchingCubes')

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(surface.GetOutputPort())
    mapper.ScalarVisibilityOff()

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    renderer.AddActor(actor)

    render_window.Render()
    interactor.Start()
