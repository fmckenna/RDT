from conans import ConanFile

class RDT(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "qmake"
    requires = "SimCenterCommonQt/0.1.5@simcenter/testing"


    default_options = {"SimCenterCommonQt:MDOFwithQt3D": True}

    def configure(self):
        if self.settings.os == "Windows":
            self.options["libcurl"].with_winssl = True
            self.options["libcurl"].with_openssl = False
