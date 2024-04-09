import ExploreContainer from '../components/ExploreContainer';
import SideNav from '../components/SideNav';
import "../App.css"
export default function Home() {
    return (
        <>
            <div className="App bg-white text-gray-600  dark:bg-gray-900 dark:text-gray-400">
                <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
                    <div className="navbar bg-blue-900 text-gray-100 w-full flex-none md:w-64">
                        <SideNav />
                    </div>
                    <div className=" grow p-6 md:overflow-y-auto md:p-12">
                        <ExploreContainer />
                    </div>
                </div>
            </div>
        </>
    )
}


